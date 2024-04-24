# Importer les fonctions nécessaires depuis les fichiers
from alphabet_et_frequences import determiner_alphabet_et_frequences
from construction_arbre import construire_arbre_huffman
from codage_texte import coder_texte
from taux_compression import determiner_taux_compression


# Définir un texte exemple
texte_exemple = "Elisa"

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


# Calculer les tailles du texte initial et compressé
taille_initial = len(texte_exemple.encode('utf-8'))
taille_compressé = len(texte_code.encode('utf-8'))

# Calculer le taux de compression
taux_compression = determiner_taux_compression(taille_initial, taille_compressé)
print("Taux de compression :", taux_compression)
