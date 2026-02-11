import sys
import os
from typing import Dict, Any, Tuple
from mazegen.generator import MazeGenerator

# ANSI Colors
RESET = "\033[0m"
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m", 
    "white": "\033[97m"
}

class MazeApp:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)
        self.width = int(self.config.get("WIDTH", 20))
        self.height = int(self.config.get("HEIGHT", 15))
        
        # Parse Entry/Exit "x,y"
        ex, ey = self.config.get("ENTRY", "0,0").split(',')
        self.entry = (int(ex), int(ey))
        fx, fy = self.config.get("EXIT", "0,0").split(',')
        self.exit = (int(fx), int(fy))
        
        self.output_file = self.config.get("OUTPUT_FILE", "maze.txt")
        self.seed = self.config.get("SEED", None)
        if self.seed: self.seed = int(self.seed)
        self.is_perfect = self.config.get("PERFECT", "True").lower() == "true"
        
        self.generator = MazeGenerator(self.width, self.height, self.seed)
        self.solution_visible = False
        self.wall_color = "white"
        self.path = []

    def load_config(self, filepath: str) -> Dict[str, str]:
        config = {}
        if not os.path.exists(filepath):
            print(f"Error: Config file '{filepath}' not found.")
            sys.exit(1)
            
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
        return config

    def run_generation(self):
        print("Generating maze...")
        self.generator = MazeGenerator(self.width, self.height, self.seed) # Reset
        self.generator.generate(self.entry, self.exit)
        
        if not self.is_perfect:
            self.generator.degrade_perfection()
            
        self.path = self.generator.solve()
        self.save_output()

    def save_output(self):
        """Writes the maze to the output file format"""
        hex_grid = self.generator.to_hex_string()
        path_str = "".join(self.path)
        
        with open(self.output_file, "w") as f:
            f.write(hex_grid)
            f.write("\n\n") # Empty line
            f.write(f"{self.entry[0]},{self.entry[1]}\n")
            f.write(f"{self.exit[0]},{self.exit[1]}\n")
            f.write(f"{path_str}\n")
        print(f"Maze saved to {self.output_file}")

    def render(self):
        """
        Renders the maze in ASCII.
        Using a 2x2 character block for each cell gives a nice look.
        Or standard +---+ style.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
        color_code = COLORS.get(self.wall_color, RESET)
        pattern_color = COLORS.get("cyan", RESET) # Couleur spécifique pour le 42
        
        # Determine path coordinates for highlighting
        path_coords = set()
        if self.solution_visible and self.path:
            cx, cy = self.entry
            path_coords.add((cx, cy))
            for move in self.path:
                if move == 'N': cy -= 1
                if move == 'E': cx += 1
                if move == 'S': cy += 1
                if move == 'W': cx -= 1
                path_coords.add((cx, cy))
        
        # Retrieve pattern cells if they exist
        pattern_cells = getattr(self.generator, 'pattern_cells', set())

        # Top border
        print(color_code + "+" + "---+" * self.width + RESET)
        
        for y in range(self.height):
            # Row content (Vertical walls)
            row_str = color_code + "|" + RESET
            for x in range(self.width):
                cell_value = self.generator.grid[y][x]
                
                # Colors
                current_color = color_code
                if (x, y) in pattern_cells:
                    current_color = pattern_color
                
                # Cell content
                if (x, y) in pattern_cells:
                    content = current_color + "███" + RESET
                elif (x, y) == self.entry: 
                    content = COLORS["green"] + " S " + RESET
                elif (x, y) == self.exit: 
                    content = COLORS["red"] + " E " + RESET
                elif (x, y) in path_coords: 
                    content = COLORS["yellow"] + " . " + RESET
                else:
                    content = "   "
                
                # Check East Wall (Bit 1 = 2)
                # If patterns cell, we color the wall too if closed
                east_wall_char = "|" if (cell_value & 2) else " "
                east_wall = current_color + east_wall_char + RESET
                
                # Note: Le mur de gauche est déjà dessiné par le caractère précédent
                row_str += content + east_wall
            print(row_str)
            
            # Row bottom (Horizontal walls)
            row_bottom = color_code + "+" + RESET
            for x in range(self.width):
                cell_value = self.generator.grid[y][x]
                
                current_color = color_code
                if (x, y) in pattern_cells:
                    current_color = pattern_color
                
                # Check South Wall (Bit 2 = 4)
                south_wall_char = "---" if (cell_value & 4) else "   "
                south_wall = current_color + south_wall_char + RESET
                
                row_bottom += south_wall + color_code + "+" + RESET
            print(row_bottom)

        print("\nControls: [r]egen, [p]ath toggle, [c]olor, [q]uit")

    def loop(self):
        self.run_generation()
        while True:
            self.render()
            cmd = input("> ").strip().lower()
            
            if cmd == 'q':
                break
            elif cmd == 'r':
                # New seed for variation
                if self.seed: self.seed += 1 
                self.run_generation()
            elif cmd == 'p':
                self.solution_visible = not self.solution_visible
            elif cmd == 'c':
                colors_list = list(COLORS.keys())
                try:
                    current_idx = colors_list.index(self.wall_color)
                    self.wall_color = colors_list[(current_idx + 1) % len(colors_list)]
                except:
                    self.wall_color = "red"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)
    
    app = MazeApp(sys.argv[1])
    app.loop()
