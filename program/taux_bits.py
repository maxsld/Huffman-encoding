from math import *

def determiner_taux_compression(taille_initial, taille_compressé):
    # Calculer le taux de compression
    taux_compression = 1 - (taille_compressé / taille_initial)
    return taux_compression

def determiner_nombre_moyen_bits(taille_compressé, nombre_caracteres):
    # Calculer le nombre moyen de bits par caractère
    nombre_moyen_bits = taille_compressé / nombre_caracteres
    return ceil(nombre_moyen_bits)

