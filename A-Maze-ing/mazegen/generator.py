from typing import List, Tuple, Set, Dict, Optional, Deque
import random
from collections import deque

class MazeGenerator:
    """
    Gestionnaire de labrinthe: Generation et Resolution.
    """
    
    # Constantes pour les murs (Bitmask)
    NORTH = 1
    EAST  = 2
    SOUTH = 4
    WEST  = 8
    
    OPPOSITE = {
        NORTH: SOUTH,
        SOUTH: NORTH,
        EAST: WEST,
        WEST: EAST
    }

    def __init__(self, width: int, height: int, seed: Optional[int] = None):
        self.width = width
        self.height = height
        if seed is not None:
            random.seed(seed)
        
        # Grille: Liste de listes d'entiers. 
        # Initialement, tous les murs sont fermés (15 = 1+2+4+8)
        self.grid = [[15 for _ in range(width)] for _ in range(height)]
        self.start: Tuple[int, int] = (0, 0)
        self.end: Tuple[int, int] = (width - 1, height - 1)

    def _get_neighbors(self, x: int, y: int) -> List[Tuple[int, int, int]]:
        """Retourne les voisins valides (x, y, direction)"""
        moves = [
            (0, -1, self.NORTH),
            (1, 0, self.EAST),
            (0, 1, self.SOUTH),
            (-1, 0, self.WEST)
        ]
        neighbors = []
        for dx, dy, direction in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((nx, ny, direction))
        return neighbors

    def add_pattern_42(self) -> None:
        """Dessine un motif '42' avec des murs pleins si la taille le permet"""
        # Motif 42 (coordonnées relatives x,y).
        # Zone de 7 de large (0..6) et 5 de haut (0..4)
        pattern = [
            # 4
            (0,0), (0,1), (0,2),        # Barre gauche haut
            (1,2),                      # Barre milieu
            (2,0), (2,1), (2,2), (2,3), (2,4), # Barre droite toute hauteur
            
            # Espace colonne 3 vide
            
            # 2
            (4,0), (5,0), (6,0),        # Haut
            (6,1),                      # Droite haut
            (4,2), (5,2), (6,2),        # Milieu
            (4,3),                      # Gauche bas (correction: c'était 6,3 avant)
            (4,4), (5,4), (6,4)         # Bas
        ]
        
        # Check size constraints (Need at least ~10x10 to be readable)
        if self.width < 10 or self.height < 10:
            # print("Warning: Maze too small for '42' pattern.") 
            # On ne print pas ici pour ne pas polluer la sortie standard requise par le sujet si c'était un script CLI pur
            # Mais c'est ok pour le debug.
            return

        offset_x = (self.width - 7) // 2
        offset_y = (self.height - 5) // 2
        
        self.pattern_cells: Set[Tuple[int, int]] = set()
        
        for px, py in pattern:
            ax, ay = offset_x + px, offset_y + py
            if 0 <= ax < self.width and 0 <= ay < self.height:
                self.grid[ay][ax] = 15 # Mur plein (North|East|South|West)
                self.pattern_cells.add((ax, ay))
    
    def generate(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Génère le labyrinthe avec l'algorithme 'Recursive Backtracker'.
        C'est l'algo le plus simple pour faire un labyrinthe 'Parfait'.
        """
        self.start = start
        self.end = end
        
        # 1. Murs du '42'
        self.add_pattern_42()
        
        # 2. Algorithme de génération (DFS itératif)
        stack = []
        visited = set()
        
        # Si on a un pattern 42, on marque ces cases comme visitées pour ne pas creuser dedans
        if hasattr(self, 'pattern_cells'):
            visited.update(self.pattern_cells)
        
        current_cell = start
        visited.add(current_cell)
        stack.append(current_cell)
        
        while stack:
            cx, cy = current_cell
            
            # Trouver les voisins non visités
            unvisited_neighbors = []
            neighbors = self._get_neighbors(cx, cy)
            
            for nx, ny, direction in neighbors:
                if (nx, ny) not in visited:
                    unvisited_neighbors.append((nx, ny, direction))
            
            if unvisited_neighbors:
                # Choisir un voisin au hasard
                nx, ny, direction = random.choice(unvisited_neighbors)
                
                # Casser le mur (Bitwise operations)
                # Enlever le mur dans la cellule courante
                self.grid[cy][cx] &= ~direction
                # Enlever le mur opposé dans la cellule voisine
                self.grid[ny][nx] &= ~self.OPPOSITE[direction]
                
                stack.append(current_cell)
                current_cell = (nx, ny)
                visited.add(current_cell)
            else:
                # Retour en arrière
                current_cell = stack.pop()
        
        # S'assurer que l'entrée et la sortie sont ouvertes sur l'extérieur
        # (Optionnel selon interprétation, mais laissé tel quel pour garder les murs de bordure)

    def degrade_perfection(self):
        """Supprime quelques murs au hasard pour créer des boucles (Labyrinthe imparfait)"""
        # On essaie de casser environ 5% du nombre total de murs restants
        attempts = (self.width * self.height) // 20
        for _ in range(attempts):
            rx, ry = random.randint(0, self.width-1), random.randint(0, self.height-1)
            neighbors = self._get_neighbors(rx, ry)
            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                # Si le mur existe, on le casse
                if (self.grid[ry][rx] & direction):
                     self.grid[ry][rx] &= ~direction
                     self.grid[ny][nx] &= ~self.OPPOSITE[direction]

    def solve(self) -> List[str]:
        """
        Résout le labyrinthe en utilisant le BFS (Breadth-First Search).
        Cela garantit le chemin le plus court.
        Retourne une liste de directions (N, E, S, W).
        """
        queue = deque([(self.start, [])]) # ( (x,y), [path] )
        visited = {self.start}
        
        while queue:
            (cx, cy), path = queue.popleft()
            
            if (cx, cy) == self.end:
                return path
            
            # Vérifier les murs pour savoir où on peut aller
            # Si le bit EST n'est PAS set, c'est qu'il n'y a pas de mur
            cell_value = self.grid[cy][cx]
            
            neighbors = self._get_neighbors(cx, cy)
            for nx, ny, direction in neighbors:
                # Si le mur est OUVERT dans cette direction
                # (cell_value & direction) == 0 signifie pas de mur
                if not (cell_value & direction):
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        direction_char = ""
                        if direction == self.NORTH: direction_char = 'N'
                        elif direction == self.EAST: direction_char = 'E'
                        elif direction == self.SOUTH: direction_char = 'S'
                        elif direction == self.WEST: direction_char = 'W'
                        
                        new_path = path + [direction_char]
                        queue.append(((nx, ny), new_path))
        return []

    def to_hex_string(self) -> str:
        """Convertit la grille en chaine hexadécimale"""
        lines = []
        for row in self.grid:
            line = "".join(f"{x:X}" for x in row)
            lines.append(line)
        return "\n".join(lines)
