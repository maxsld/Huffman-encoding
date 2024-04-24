# Importer les fonctions nécessaires depuis les fichiers
from alphabet_et_frequences import determiner_alphabet_et_frequences
from construction_arbre import construire_arbre_huffman
from codage_texte import coder_texte
from taux_bits import determiner_taux_compression, determiner_nombre_moyen_bits


# # Définir un texte exemple
# texte_exemple = "Ceci est un test d'encode avec Huffman"

# print(f"Nom a encodé : " , texte_exemple)
# # Étape 1 : Détermination de l'alphabet et des fréquences
# alphabet_et_frequences = determiner_alphabet_et_frequences(texte_exemple)
# print("Alphabet et fréquences :", alphabet_et_frequences)

# # Étape 2 : Construction de l'arbre de codage de Huffman
# arbre_huffman = construire_arbre_huffman(alphabet_et_frequences)
# print("Arbre de Huffman construit.")

# # Étape 3 : Codage du texte
# texte_code = coder_texte(texte_exemple, arbre_huffman)
# print("Texte codé :", texte_code)


# # Calculer les tailles du texte initial et compressé
# taille_initial = len(texte_exemple.encode('utf-8'))
# taille_compressé = len(texte_code.encode('utf-8'))

# # Calculer le taux de compression
# taux_compression = determiner_taux_compression(taille_initial, taille_compressé)
# print("Taux de compression :", taux_compression)

# # Déterminé le nombre de bits

# taille_compressé_bits = len(texte_code)
# nombre_caracteres = len(texte_exemple)

# nombre_moyen_bits = determiner_nombre_moyen_bits(taille_compressé_bits, nombre_caracteres)
# print("Nombre moyen de bits par caractère dans le texte compressé :", nombre_moyen_bits)


# Fonction pour lire le contenu d'un fichier texte
def lire_fichier_texte():
    with open("../data/textesimple.txt", 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    return contenu

# Fonction pour écrire les fréquences de caractère dans un fichier
def ecrire_frequences(nom_fichier, alphabet_et_frequences):
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(str(len(alphabet_et_frequences)) + '\n')
        for caractere, freq in alphabet_et_frequences:
            fichier.write(caractere + ' ' + str(freq) + '\n')

# Lecture du fichier texte
texte = lire_fichier_texte()

# Détermination de l'alphabet et des fréquences
alphabet_et_frequences = determiner_alphabet_et_frequences(texte)

# Construction de l'arbre de codage de Huffman
arbre_huffman = construire_arbre_huffman(alphabet_et_frequences)

# Codage du texte
texte_code = coder_texte(texte, arbre_huffman)

# Écriture du texte compressé dans un fichier
with open("../data/textesimple_comp.bin", 'wb') as fichier:
    fichier.write(texte_code.encode('utf-8'))

# Écriture des fréquences de caractère dans un fichier
ecrire_frequences("../data/textesimple_freq.txt", alphabet_et_frequences)

print("Compression terminée.")
