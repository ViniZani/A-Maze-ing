
# A-Maze-ing

*This project has been created as part of the 42 curriculum by vzani-st, kbentes-.*

---

## Description
**A-Maze-ing** is a procedural maze generator focused on robustness and logical validation. The project was developed to create fully usable mazes that respect strict structural constraints, always guaranteeing a valid path between entry and exit points. It explores fundamental concepts of Graph Theory, search algorithms, and data structures, offering an interactive command-line interface for visualization and file exportation.

## 🛠 Instructions

### Installation
The project uses a `Makefile` to facilitate setup across different operating systems. It is recommended to use a Python 3.10+ environment.

```bash
# Creates the virtual environment and installs dependencies (dotenv, flake8, mypy)
make install
```
### Execution
To run the program using a configuration file:

```bash
# In Linux/macOS
make run
```

### Code Quality (Linting)
To verify that the code follows PEP8 standards and static typing:

```bash
make lint           # Basic verification
make lint-strict    # Strict verification with Mypy
```
### Configuration File Description
The program reads a file (e.g., config.txt) in KEY=VALUE format. The following fields are mandatory:

- WIDTH: Maze width (positive integer).

- HEIGHT: Maze height (positive integer).

- ENTRY: Starting coordinates in x,y format.

- EXIT: Ending coordinates in x,y format.

- OUTPUT_FILE: Path to the file where the hexadecimal maze and the path will be saved.

- PERFECT: True for perfect mazes (no loops/cycles) or False for mazes with alternative paths.

### Chosen Maze Algorithm
The algorithm chosen for maze generation was Randomized Depth-First Search (DFS), also known as the "Iterative Backtracking" algorithm.

Reason for choosing this algorithm
DFS was chosen for its efficiency in generating "perfect" mazes with long corridors and complex branching, providing an interesting visual and logical challenge. Furthermore, its implementation via a stack is highly performant and easy to validate against unwanted cycles, allowing precise control over the connectivity of each cell.

### Maze Generator Module Documentation
The mazegen/ directory acts as a reusable module.

How to Instantiate and Use
```python
from mazegen.generator import MazeGenerator
```

#### Instantiate the generator with dimensions and control points
```python
generator = MazeGenerator(width=20, height=10, origin=(0,0), final=(19,9))
```

#### Generate the internal structure
```python
generator.generate()
```

#### The grid can be accessed for custom rendering
```python
grid = generator.grid 
Custom Parameters
width (int): Number of columns.

height (int): Number of rows.

origin/final (tuple): (x, y) coordinates for start and end.

seed (int, optional): Seed for deterministic generation.

perfect (bool): Defines if the maze will have cycles or be a strict tree.
```
### Team and Project Management
vzani-st: Responsible for the DFS algorithm logic, the mazegen module structure, and the ASCII rendering system.

kbentes-: Responsible for the code review, organizate the project search algorithms (BFS) for solving, system.

### Planning and Evolution
The initial planning consisted of three phases: Data Structure, Generation Algorithm, and Interface. During development, we realized the need for an extra "Type Sanitization" phase to pass the rigorous Mypy tests. While this delayed the final polishing of the UI, it significantly increased the system's stability.

### Successes and Improvements
What worked well: Separating the generation engine (mazegen) from the interface logic (renderer) allowed for isolated algorithm testing.

What could be improved: The ANSI color system works perfectly on Linux/macOS but required additional adjustments for older Windows terminals.

Tools Used:
- Python 3.10+: Core language.

- Flake8/Mypy: Style and typing assurance.

- Make: Task automation.

- Git: Version control.

### Resources

- Wikipedia: Maze Generation Algorithms

- Search A Maze For Any Path - Depth First Search Fundamentals (Similar To "The Maze" on Leetcode)- https://www.youtube.com/watch?v=W9F8fDQj7Ok

- DFS - Busca em profundidade em grafos - https://www.youtube.com/watch?v=2ZN8cHp8ZZI


- Curso Python #11 - Cores no Terminal - https://www.youtube.com/watch?v=0hBIhkcA8O8

- Breadth First Search (BFS): Visualized and Explained - https://www.youtube.com/watch?v=xlVX7dXLS64&t=45s


- 5.1 Graph Traversals - BFS & DFS -Breadth First Search and Depth First Search - https://www.youtube.com/watch?v=pcKY4hjDrxk

### AI Usage
Artificial Intelligence was utilized in this project for the following tasks:

Code Refactoring: Assistance in converting functions to meet rigorous Flake8 and Mypy standards (linting).

Environment Bug Fixing: Diagnosing compatibility errors between Unix Makefiles and Windows PowerShell.

Documentation: Initial structuring of Docstrings following the PEP 257 standard.

Optimization: Used to anwser pontual questions.