# Documentation du Projet A-Maze-ing

## 1. Vue d'Ensemble

**Nom du Projet :** A-Maze-ing  
**Version :** 1.3  
**Langage :** Python 3.10+  
**Objectif :** Développer un système complet de génération, résolution et visualisation de labyrinthes. Le projet met en œuvre des concepts Python avancés (typage, classes, gestionnaires de contexte) et la Théorie des Graphes algorithmique.

### Architecture Technique
Le projet est divisé en trois couches distinctes pour assurer modularité et réutilisabilité (principes SOLID) :
1.  **Couche Logique (MazeGenerator)** : Une classe autonome responsable de la structure de données, des algorithmes de génération et de la logique de résolution. Elle ne gère **aucune** entrée/sortie ni affichage. C'est le "Cerveau".
2.  **Couche Application (MazeApp)** : Le chef d'orchestre. Elle gère le parsing du fichier de configuration, les opérations d'E/S (lecture/écriture disque) et la boucle d'interaction utilisateur.
3.  **Couche Présentation (Renderer)** : Responsable de traduire la grille de données abstraite en un format visuel compréhensible pour l'humain (ASCII Art sur le terminal).

### Concepts Clés
*   **Opérations Bit à Bit (Bitwise)** :
    Chaque cellule est un entier représentant ses 4 murs. C'est la méthode la plus efficace en mémoire.
    *   Nord = 1 (`0001`), Est = 2 (`0010`), Sud = 4 (`0100`), Ouest = 8 (`1000`).
    *   Une cellule totalement fermée vaut 15 (`1111`).
    *   Pour savoir si un passage est ouvert au Sud : `if (cell & 4) == 0`.
    *   Pour casser un mur au Sud : `cell &= ~4` (Inverse bitwise combine avec AND).
*   **Théorie des Graphes** : Le labyrinthe **EST** un graphe. Les cellules sont les noeuds, les passages sont les arêtes.
    *   **Génération** : Recherche en Profondeur (DFS) via l'algorithme "Recursive Backtracker".
    *   **Résolution** : Recherche en Largeur (BFS) pour garantir mathématiquement le chemin le plus court.
*   **Context Managers** : Utilisation stricte de l'instruction `with` pour toute manipulation de fichier afin d'éviter les fuites de ressources ou fichiers corrompus.

---

## 2. Guide d'Implémentation des Fonctionnalités

### A. Analyse de Configuration (Parsing)
**Description :** L'application démarre par la lecture d'un fichier `config.txt` ligne par ligne.
**Détails Techniques :**
*   Ouverture du fichier en mode lecture (`r`).
*   Filtrage des lignes vides ou commençant par `#`.
*   Séparation (split) sur le caractère `=`. Attention à ne split que sur le *premier* égal.
*   **Validation des données** :
    *   `WIDTH`/`HEIGHT` doivent être convertis en `int`.
    *   `PERFECT` doit être converti en `bool` ("True"/"False").
    *   `ENTRY`/`EXIT` ("x,y") doivent être splittés puis convertis en `tuple` d'entiers.

### B. Génération de Labyrinthe Parfait
**Définition :** Un labyrinthe parfait est un "Arbre Couvrant" (Spanning Tree) sur le graphe de la grille.
**Propriétés mathématiques :**
1.  **Connexité** : Toutes les cellules sont accessibles. Il n'y a pas d'îlots isolés.
2.  **Acyclique** : Il n'existe AUCUNE boucle.
3.  **Unicité du chemin** : Il existe exactement UN et un seul chemin entre deux points quelconques.
**Implémentation :** Voir feuille de route algorithmique ci-dessous.

### C. Génération de Labyrinthe Imparfait
**Description :** Introduit des boucles, offrant plusieurs chemins possibles pour atteindre la sortie.
**Implémentation :**
1.  Générer d'abord un labyrinthe **Parfait**.
2.  Lancer une méthode `degrade_perfection()` :
    *   Sélectionner aléatoirement X coordonnées dans la grille.
    *   Pour chaque cellule choisie, sélectionner un mur existant au hasard.
    *   Abattre ce mur.
    *   Cela crée instantanément une connexion supplémentaire, donc une boucle (cycle) dans le graphe.

### D. Le Motif "42"
**Description :** Un ensemble de cellules doit rester totalement muré (valeur 15) pour former visuellement le nombre "42".
**Stratégie :**
*   Définir une liste de coordonnées relatives `(dx, dy)` pour dessiner les barres du 4 et du 2.
*   Calculer le décalage (offset) pour centrer ce motif dans la grille actuelle (`(Width - PatternWidth) // 2`).
*   **Avant** le début de la génération algorithmique : Marquer ces cellules comme "Visitées" dans le set `visited` et s'assurer que leur valeur est `15`.
*   L'algorithme de génération contournera naturellement ces cellules car elles sont déjà "visitées".

### E. Export Hexadécimal
**Format :** Chaque ligne du fichier représente une ligne du labyrinthe. Chaque caractère est un chiffre hexa (0-F).
**Conversion :**
*   Valeur 0 (0000) -> '0' (Tout ouvert, carrefour)
*   Valeur 15 (1111) -> 'F' (Tout fermé, bloc plein)
*   Exemple : Mur Est et Sud fermés (2 + 4 = 6) -> '6'.
*   En Python : `format(valeur, 'X')` convertit l'entier en string Hex majuscule.

---

## 3. Feuille de Route : Algorithme (MazeGenerator)

Cette section détaille la logique interne de la classe `MazeGenerator`.

### Étape 1 : Initialisation des Structures
Créer une matrice 2D (liste de listes).
Chaque case est initialisée à `15` (`1 | 2 | 4 | 8`), c'est-à-dire une boîte totalement fermée.

### Étape 2 : Logique de Voisinage
Créer une méthode privée `_get_neighbors(x, y)` qui renvoie les voisins valides.
*   Vérifier les limites de la grille (`0 <= nx < width`).
*   Retourner une liste de tuples : `(x_voisin, y_voisin, DIRECTION)`.
*   Note : La direction est celle pour *aller* vers le voisin (ex: si voisin est à droite, direction = EST).

### Étape 3 : Le Mécanisme de "Creusage" (Carve)
Pour connecter la `Cellule A` à la `Cellule B` située à l'Est :
1.  Dans `Cellule A`, on retire le mur EST : `grid[y][x] &= ~EAST` (Le bit 2 passe à 0).
2.  Dans `Cellule B`, on retire le mur OUEST : `grid[y][x+1] &= ~WEST` (Le bit 8 passe à 0).
C'est symétrique. Si on oublie l'étape 2, le mur n'est ouvert que d'un côté !

### Étape 4 : Le Recursive Backtracker (Itératif)
Pourquoi itératif ? La récursion standard de Python plante sur les grands labyrinthes (limite de la pile d'appels). On utilise donc une "Pile" manuelle (une liste).

1.  Initialiser `Stack = []` (Liste LIFO) et `Visited = set()`.
2.  Choisir la case de départ `(0,0)`, l'ajouter à `Stack` et à `Visited`.
3.  **Tant que** `Stack` n'est pas vide :
    *   Prendre la cellule courante (`current`) au sommet de la pile (sans la retirer pour l'instant : `stack[-1]`).
    *   Scanner tous ses voisins. Filtrer pour garder uniquement ceux qui **ne sont pas dans `Visited`**.
    *   **Cas 1 : Il reste des voisins non visités**
        *   En choisir un au hasard (Random).
        *   "Creuser" le mur entre `current` et ce `voisin`.
        *   Ajouter le `voisin` à `Stack`.
        *   Ajouter le `voisin` à `Visited`.
        *   (La boucle recommence, le `voisin` devient le nouveau `current`).
    *   **Cas 2 : Cul-de-sac (Tous les voisins sont visités)**
        *   On retire l'élément de la pile : `stack.pop()`.
        *   (On revient donc à la case précédente ("Backtrack") pour voir si elle a d'autres chemins possibles).

### Étape 5 : Résolution (BFS)
1.  Initialiser une `File` (Queue FIFO) avec `[(StartCell, CheminActuel)]`.
2.  Initialiser `Visited = {StartCell}`.
3.  **Tant que** la File n'est pas vide :
    *   Défiler (`popleft`) l'élément `(current, path)`.
    *   Si `current == Exit` : **Victoire**, retourner `path`.
    *   Pour chaque voisin de `current` :
        *   **CRITIQUE** : Vérifier s'il y a un mur ! `if not (grid[y][x] & DIRECTION)`.
        *   Si PAS de mur et voisin PAS visité :
            *   Ajouter voisin à `Visited`.
            *   Mettre à jour le chemin : `new_path = path + [DIRECTION_CHAR]`.
            *   Enfiler `(voisin, new_path)`.

---

## 4. Feuille de Route : Graphismes (Rendu ASCII)

Comment dessiner une grille complexe ligne par ligne dans un terminal ?

### Concept
On ne peut pas dessiner une case entière puis passer à la suivante à droite, car le terminal écrit par lignes de texte horizontales.
Il faut dessiner la **partie supérieure** de toutes les cases de la ligne 1, puis la **partie inférieure** de toutes les cases de la ligne 1.

### Étape 1 : Pré-calculs
*   Définir les couleurs ANSI.
*   Calculer les coordonnées du chemin de solution (si activé) pour savoir quelles cases surligner.

### Étape 2 : La Bordure Supérieure
Avant tout, on imprime un toit : `+` suivi de `---+` répété `Width` fois.

### Étape 3 : La Boucle de Rendu (Pour chaque Ligne Y)

    **Passage 1 : Le Corps de la cellule (Murs verticaux)**
    *   Commencer la ligne de texte par `|`. (C'est le mur Ouest de la toute première case).
    *   Pour chaque cellule X de la ligne :
        *   **Contenu** : Décider quoi afficher au centre (Espaces vides "   ", " S " pour Start, " . " pour le chemin, "███" pour le Pattern 42).
        *   **Mur Est** : Vérifier le bit EST (`cell & 2`).
            *   Si 1 (fermé) : Ajouter `|` à la string.
            *   Si 0 (ouvert) : Ajouter ` ` (espace) appelé "portes".
    *   Imprimer la ligne complète.

    **Passage 2 : Le Sol de la cellule (Murs horizontaux)**
    *   Commencer par un coin `+`.
    *   Pour chaque cellule X de la ligne :
        *   **Mur Sud** : Vérifier le bit SUD (`cell & 4`).
            *   Si 1 (fermé) : Ajouter `---`.
            *   Si 0 (ouvert) : Ajouter `   `.
        *   Ajouter un coin `+`.
    *   Imprimer la ligne complète.

### Étape 4 : Boucle d'Interaction
Enfermer l'appel `render()` dans une boucle `while` pour permettre le rafraîchissement dynamique :
1.  Effacer l'écran (`os.system('clear')`).
2.  Appeler `render()`.
3.  Demander une entrée utilisateur (`input`).
4.  Si 'r' -> Regénérer (incrémenter Seed).
5.  Si 'p' -> Inverser le booléen `show_solution`.
6.  Si 'c' -> Changer la couleur courante.
