def coder_texte(texte, arbre_huffman):
    # Dictionnaire pour stocker les codes de Huffman associés à chaque caractère
    codes = {}

    # Fonction récursive pour générer les codes de Huffman à partir de l'arbre de Huffman
    def generer_codes(noeud, code_actuel=""):
        if noeud:
            if noeud.caractere is not None:
                codes[noeud.caractere] = code_actuel
            generer_codes(noeud.gauche, code_actuel + "0")
            generer_codes(noeud.droit, code_actuel + "1")

    generer_codes(arbre_huffman)

    # Initialiser une chaîne pour stocker le texte encodé final
    texte_code_final = ""

    # Parcourir chaque caractère dans le texte et ajouter son code correspondant
    for caractere in texte:
        texte_code_final += codes[caractere]

    return texte_code_final
