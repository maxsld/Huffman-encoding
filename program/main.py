# Importer les fonctions nécessaires depuis les fichiers
from alphabet_et_frequences import determiner_alphabet_et_frequences
from construction_arbre import construire_arbre_huffman
from codage_texte import coder_texte
from taux_bits import determiner_taux_compression, determiner_nombre_moyen_bits
import os
from bitarray import bitarray

'''
texte_exemple = "Ceci est un test d'encode avec Huffman"
print(f"Nom a encodé : " , texte_exemple)

# Étape 1 : Détermination de l'alphabet et des fréquences
alphabet_et_frequences = determiner_alphabet_et_frequences(texte_exemple)
print("Alphabet et fréquences :", alphabet_et_frequences)

# Étape 2 : Construction de l'arbre de codage de Huffman
arbre_huffman = construire_arbre_huffman(alphabet_et_frequences)
print("Arbre de Huffman construit.")

# Étape 3 : Codage du texte
texte_code = coder_texte(texte_exemple, arbre_huffman)
print("Texte codé :", texte_code)


# Étape 4 : Calculer les tailles du texte initial et compressé

# Calculer la taille du fichier texte initial
taille_texte_initial = len(texte_exemple)

# Calculer la taille du fichier compressé
taille_texte_compresse = len(texte_code) // 8  # Convertir la taille en octets (8 bits par octet)

# Calculer le taux de compression
taux_compression = 1 - (taille_texte_compresse / taille_texte_initial)

print("Taux de compression :", taux_compression)


# Étape 5 : Déterminé le nombre de bits

taille_compressé_bits = len(texte_code)
nombre_caracteres = len(texte_exemple)

nombre_moyen_bits = determiner_nombre_moyen_bits(taille_compressé_bits, nombre_caracteres)
print("Nombre moyen de bits par caractère dans le texte compressé :", nombre_moyen_bits)
'''


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


def ecrire_fichier_binaire(nom_fichier, contenu_binaire):
    try:
        with open(nom_fichier, 'wb') as fichier:
            contenu_binaire.tofile(fichier)
            print("\nFichier {} créé avec succès.".format(nom_fichier))
    except IOError:
        print("Erreur lors de l'écriture dans le fichier.")
    except Exception as e:
        print("Une erreur s'est produite :", e)


def compression_huffman(nom_fichier):
    # Suppression des fichiers existants s'ils existent
    nom_fichier_compr = "./fichier_compresses/{}_compr.bin".format(nom_fichier.split('/')[-1].split('.')[0])
    nom_fichier_freq = "./fichier_compresses/{}_freq.txt".format(nom_fichier.split('/')[-1].split('.')[0])
    
    if os.path.exists(nom_fichier_compr):
        os.remove(nom_fichier_compr)
        print("Fichier {} supprimé.".format(nom_fichier_compr))
    
    if os.path.exists(nom_fichier_freq):
        os.remove(nom_fichier_freq)
        print("Fichier {} supprimé.".format(nom_fichier_freq))

    # Lecture du fichier texte
    texte = lire_fichier_texte(nom_fichier)

    # Détermination de l'alphabet et des fréquences
    alphabet_et_frequences = determiner_alphabet_et_frequences(texte)

    # Construction de l'arbre de codage de Huffman
    arbre_huffman = construire_arbre_huffman(alphabet_et_frequences)

    # Codage du texte
    texte_code = coder_texte(texte, arbre_huffman)

    # Convertir le texte compressé en une séquence de bits
    texte_binaire = bitarray()
    texte_binaire.extend(texte_code)

    # Écriture du texte compressé dans un fichier binaire
    nom_fichier_compr = "./fichier_compresses/{}_compr.bin".format(nom_fichier.split('/')[-1].split('.')[0])
    ecrire_fichier_binaire(nom_fichier_compr, texte_binaire)

    # Écriture des fréquences de caractère dans un fichier
    nom_fichier_freq = "./fichier_compresses/{}_freq.txt".format(nom_fichier.split('/')[-1].split('.')[0])
    ecrire_frequences(nom_fichier_freq, alphabet_et_frequences)

    print("\nCompression terminée.")

    # Calculer les tailles du texte initial et compressé
    taille_texte_initial = os.path.getsize(nom_fichier)  # Taille du fichier initial
    taille_texte_compresse = os.path.getsize(nom_fichier_compr)
    taux_compression = round((1 - (taille_texte_compresse / taille_texte_initial))*100 , 2)
    print("\nTaux de compression :", taux_compression, "%")

    # Calculer le nombre moyen de bits par caractère dans le texte compressé
    texte_initial = len(texte)
    taille_compressé_bits = len(texte_code)
    nombre_moyen_bits = determiner_nombre_moyen_bits(taille_compressé_bits, texte_initial)
    print("Nombre moyen de bits par caractère dans le texte compressé :", nombre_moyen_bits)

# Utilisation de la fonction de compression
compression_huffman("./data/alice.txt")
