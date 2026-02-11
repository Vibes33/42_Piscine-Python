_This project has been created as part of the 42 curriculum by Ryan._

# A-Maze-ing

## Description
A-Maze-ing is a Python-based maze generator and visualizer. It generates random mazes of variable sizes, allows for custom configuration (entry/exit points, seeds, perfection), and provides an interactive ASCII interface to explore the maze and view the shortest path solution.

## Instructions

### Installation
```bash
make install
```

### Execution
```bash
make run
# OR
python3 a_maze_ing.py config.txt
```

### Controls (Interactive Mode)
- **r**: Re-generate the maze (increments seed if set).
- **p**: Toggle the solution path (Shortest Path).
- **c**: Cycle through wall colors.
- **q**: Quit the program.

## Configuration (config.txt)
The configuration file uses `KEY=VALUE` pairs.
- `WIDTH`: Width of the maze (integer).
- `HEIGHT`: Height of the maze (integer).
- `ENTRY`: Start coordinates x,y (e.g., 0,0).
- `EXIT`: End coordinates x,y (e.g., 19,14).
- `OUTPUT_FILE`: Filename for the raw output.
- `PERFECT`: `True` for a perfect maze (no loops), `False` for imperfect.
- `SEED`: Integer seed for reproducibility.

## Algorithm
We use the **Recursive Backtracker** algorithm (implemented iteratively to handle large sizes). 
1. Choose a starting cell and mark it as visited.
2. If the current cell has unvisited neighbors:
   a. Push current cell to stack.
   b. Choose a random unvisited neighbor.
   c. Remove the wall between them.
   d. Make the chosen neighbor the current cell and mark as visited.
3. Else, pop a cell from the stack.
4. Repeat until stack is empty.

**Why this algorithm?**
It guarantees a "Perfect Maze" (a Spanning Tree), meaning there is exactly one unique path between any two points, with no loops. It creates long, winding corridors which look great visually.

## Reusability
The logic is encapsulated in the `mazegen` package.
Can be built using `make package`.

Usage example:
```python
from mazegen.generator import MazeGenerator

gen = MazeGenerator(20, 15)
gen.generate((0,0), (19,14))
path = gen.solve()
print(gen.to_hex_string())
```

## Team
- **Ryan**: Lead Developer (Logic, CLI, Documentation)
