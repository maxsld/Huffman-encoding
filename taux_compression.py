def determiner_taux_compression(taille_initial, taille_compressé):
    # Calculer le taux de compression
    taux_compression = 1 - (taille_compressé / taille_initial)
    return taux_compression
