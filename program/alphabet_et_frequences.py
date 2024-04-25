def determiner_alphabet_et_frequences(texte):
    alphabet = {}
    for caractere in texte:
        if caractere in alphabet:
            alphabet[caractere] += 1
        else:
            alphabet[caractere] = 1
    
    # Trier l'alphabet en fonction des fréquences croissantes et des valeurs ASCII des caractères
    alphabet_trie = sorted(alphabet.items(), key=lambda x: (x[1], ord(x[0])))

    return alphabet_trie

# Exemple d'utilisation :
# texte_exemple = "ceci est un test avec beaucoup de lettres"
# alphabet_et_frequences = determiner_alphabet_et_frequences(texte_exemple)
# print("Alphabet et fréquences :", alphabet_et_frequences)
