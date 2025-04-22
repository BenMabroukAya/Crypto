# Cryptographie - Méthodes de Chiffrement/Déchiffrement

Ce dépôt contient une collection de méthodes implémentées en Python pour le chiffrement et déchiffrement de textes. Chaque méthode offre une approche différente de la cryptographie, avec ses propres avantages et inconvénients.

## Qu'est-ce que le cryptage ?

Le cryptage est le processus de conversion d'un texte lisible (clair) en une forme illisible (chiffré) pour protéger sa confidentialité. Le déchiffrement est le processus inverse qui permet de retrouver le texte original.

## Méthodes Disponibles

### 1. ADFGVX
- **Description** : Chiffrement par substitution et transposition utilisé pendant la Première Guerre mondiale.
- **Avantages** : Double protection (substitution + transposition), résistant aux analyses de fréquence simples.
- **Inconvénients** : Clé complexe, relativement lent à mettre en œuvre.

### 2. César (cesarr)
- **Description** : Chiffrement par décalage simple où chaque lettre est remplacée par une autre à distance fixe.
- **Avantages** : Simple à comprendre et implémenter.
- **Inconvénients** : Très vulnérable aux attaques par force brute et analyse de fréquence.

### 3. Chiffrement Affine (ChAffine, cryptAffine)
- **Description** : Combinaison de deux opérations mathématiques (multiplication et addition) pour chaque caractère.
- **Avantages** : Plus sécurisé que César grâce à deux clés.
- **Inconvénients** : Nécessite que la première clé soit première avec la taille de l'alphabet.

### 4. Cryptanalyse par Fréquence (AnalyseFreq, exerciceanalysedefrequence)
- **Description** : Méthode pour déchiffrer des textes en analysant la fréquence des lettres.
- **Avantages** : Efficace contre les chiffrements simples comme César.
- **Inconvénients** : Moins efficace sur les textes courts ou avec des chiffrements complexes.

### 5. Chiffrement Horizontal (cryptHorizontale)
- **Description** : Transposition des lettres en les écrivant dans une grille ligne par ligne puis en les lisant colonne par colonne.
- **Avantages** : Masque les motifs de fréquence.
- **Inconvénients** : Vulnérable si la taille de la grille est devinée.

### 6. RSA
- **Description** : Cryptographie asymétrique utilisant des clés publique/privée.
- **Avantages** : Sécurité élevée, adapté aux échanges sécurisés.
- **Inconvénients** : Lent, nécessite une gestion complexe des clés.

### 7. Transposition (Transpo)
- **Description** : Réarrangement des lettres selon un motif spécifique.
- **Avantages** : Simple à implémenter.
- **Inconvénients** : Vulnérable si le motif de transposition est découvert.

## Utilisation

Chaque fichier Python contient une implémentation spécifique d'une méthode de cryptographie. Exécutez le fichier correspondant à la méthode souhaitée et suivez les instructions fournies dans le code.

## Contribution

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou une pull request pour toute amélioration ou correction.

## License
MIT © 2025 [Aya Ben Mabrouk]