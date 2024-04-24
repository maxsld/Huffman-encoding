class Noeud:
    def __init__(self, caractere=None, freq=0):
        self.caractere = caractere
        self.freq = freq
        self.gauche = None
        self.droit = None

def construire_arbre_huffman(alphabet_et_frequences):
    arbres = [Noeud(caractere, freq) for caractere, freq in alphabet_et_frequences]
    
    while len(arbres) > 1:
        # Tri des arbres par fréquence
        arbres.sort(key=lambda x: x.freq)
        
        # Sélection des deux arbres de fréquence minimale
        t1 = arbres.pop(0)
        t2 = arbres.pop(0)
        
        # Création d'un nouvel arbre avec t1 et t2 comme sous-arbres
        nouveau_noeud = Noeud(freq=t1.freq + t2.freq)
        nouveau_noeud.gauche = t1
        nouveau_noeud.droit = t2
        
        # Ajout du nouvel arbre à la liste
        arbres.append(nouveau_noeud)
    
    # L'arbre final est le seul élément restant dans la liste
    return arbres[0]
