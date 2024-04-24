def coder_texte(texte, arbre_huffman):
    codes = {}

    def generer_codes(noeud, code_actuel=""):
        if noeud:
            if noeud.caractere is not None:
                codes[noeud.caractere] = code_actuel
            generer_codes(noeud.gauche, code_actuel + "0")
            generer_codes(noeud.droit, code_actuel + "1")

    generer_codes(arbre_huffman)
    texte_code_final = ""
    for caractere in texte:
        texte_code_final += codes[caractere]

    return texte_code_final
