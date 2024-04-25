import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from alphabet_et_frequences import determiner_alphabet_et_frequences
from construction_arbre import construire_arbre_huffman
from codage_texte import coder_texte
from taux_bits import determiner_taux_compression, determiner_nombre_moyen_bits
import os
import threading
import time
import subprocess

# Fonction pour lire le contenu d'un fichier texte
def lire_fichier_texte(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    return contenu

# Fonction pour écrire les fréquences de caractère dans un fichier
def ecrire_frequences(nom_fichier, alphabet_et_frequences):
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(str(len(alphabet_et_frequences)) + '\n')
        for caractere, freq in alphabet_et_frequences:
            fichier.write(caractere + ' ' + str(freq) + '\n')
        print("Fichier {} créé avec succès.".format(nom_fichier))

# Fonction pour écrire le contenu dans un fichier
def ecrire_fichier_texte(nom_fichier, contenu):
    try:
        with open(nom_fichier, 'w') as fichier:
            fichier.write(contenu)
            print("\nFichier {} créé avec succès.".format(nom_fichier))
    except IOError:
        print("Erreur lors de l'écriture dans le fichier.")
    except Exception as e:
        print("Une erreur s'est produite :", e)

# Fonction de compression Huffman
def compression_huffman(nom_fichier_entree, progress_bar):
    # Lecture du fichier texte
    texte = lire_fichier_texte(nom_fichier_entree)

    # Détermination de l'alphabet et des fréquences
    alphabet_et_frequences = determiner_alphabet_et_frequences(texte)

    # Construction de l'arbre de codage de Huffman
    arbre_huffman = construire_arbre_huffman(alphabet_et_frequences)

    # Codage du texte
    texte_code = coder_texte(texte, arbre_huffman)

    # Création du dossier pour les fichiers compressés s'il n'existe pas
    dossier_sortie = os.path.abspath("./fichier_compresses/")
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    # Écriture du texte compressé dans un fichier
    nom_fichier_sortie = os.path.join(dossier_sortie, "{}_compr.bin".format(os.path.basename(nom_fichier_entree).split('.')[0]))
    ecrire_fichier_texte(nom_fichier_sortie, texte_code)

    # Écriture des fréquences de caractère dans un fichier
    nom_fichier_freq = os.path.join(dossier_sortie, "{}_freq.txt".format(os.path.basename(nom_fichier_entree).split('.')[0]))
    ecrire_frequences(nom_fichier_freq, alphabet_et_frequences)

    # Mise à jour de la barre de progression
    progress_bar["value"] = 100

    # Affichage du message de confirmation
    afficher_confirmation()

    # Ouvrir l'explorateur de fichiers dans le dossier où sont les fichiers compressés
    ouvrir_explorateur(dossier_sortie)

# Fonction pour afficher le message de confirmation après la compression
def afficher_confirmation():
    confirmation_label = tk.Label(root, text="Compression terminée.")
    confirmation_label.pack()

# Fonction pour ouvrir l'explorateur de fichiers dans un dossier spécifique
def ouvrir_explorateur(dossier):
    subprocess.Popen(['explorer', dossier])

# Fonction pour sélectionner un fichier à compresser
def choisir_fichier():
    fichier_entree = filedialog.askopenfilename(title="Sélectionner un fichier texte à compresser", filetypes=[("Fichiers texte", "*.txt")])
    if fichier_entree:
        # Affichage de la barre de progression
        progress_bar.pack(pady=10)
        # Lancement de la compression dans un thread
        threading.Thread(target=compression_huffman, args=(fichier_entree, progress_bar)).start()

# Création de l'interface tkinter
root = tk.Tk()
root.title("Compression de fichiers avec Huffman")
root.geometry("700x250")

# Label titre
titre_label = tk.Label(root, text="Compression de fichiers avec Huffman", font=("Helvetica", 16))
titre_label.pack(pady=10)

# Barre de progression
progress_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate")

# Bouton pour sélectionner un fichier à compresser
btn_choisir_fichier = tk.Button(root, text="Choisir un fichier", command=choisir_fichier)
btn_choisir_fichier.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
