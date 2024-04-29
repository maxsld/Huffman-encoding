# Projet de Compression de Données avec Codage de Huffman

**Objectif du Projet:**
Ce projet vise à mettre en œuvre l'algorithme semi-adaptatif de Huffman pour la compression de données. L'algorithme de Huffman est une méthode statistique de compression sans perte qui remplace les caractères fréquents par de courtes séquences de bits et les caractères moins fréquents par des séquences plus longues. L'objectif principal est de réduire la taille des fichiers tout en conservant l'intégrité des données, ce qui permet un stockage plus efficace et une transmission plus rapide sur les réseaux.

**Prérequis:**
- Python doit être installé sur votre système. Si Python n'est pas installé, vous pouvez le télécharger à partir du site officiel de Python : https://www.python.org/downloads/
- Le module Tkinter est utilisé pour l'interface utilisateur graphique (GUI). Si vous n'avez pas encore Tkinter, vous pouvez l'installer en exécutant la commande suivante dans votre terminal :
  ```
  pip install tk
  ```

- La bibliothèque bitarray est utilisée pour manipuler efficacement les séquences de bits. Vous pouvez l'installer en exécutant la commande suivante dans votre terminal :
  ```
  pip install bitarray
  ```

**Utilisation:**
Ce projet comprend deux fichiers principaux :
- Le fichier `main.py` permet d'exécuter le programme dans la console, offrant une interface en ligne de commande pour interagir avec le programme.
  ```
  python main.py
  ```
- Le fichier `InterfaceUI.py` permet d'exécuter le programme avec une interface utilisateur en Tkinter, offrant une expérience plus conviviale pour l'utilisateur.

**Instructions:**
- Les fichiers texte à encoder doivent être placés dans le dossier nommé `data`.
- Les fichiers encodés seront ajoutés dans un dossier nommé `fichiers_compresses`.

**Fonctionnalités:**
1. Détermine l'alphabet et les fréquences de caractères dans un texte donné.
2. Construit l'arbre de codage de Huffman en utilisant les fréquences des caractères.
3. Code et compresse le texte initial en remplaçant les caractères par leurs séquences binaires correspondantes.
4. Calcule le taux de compression obtenu après la compression.
5. Détermine le nombre moyen de bits de stockage d'un caractère dans le texte compressé.
6. Fournit une interface utilisateur conviviale pour une utilisation plus intuitive.

**Auteur:**
SOLDAN Maxens
