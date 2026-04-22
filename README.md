# A-Maze-ing
Generate a fully usable maze that respects structural constraints and guarantees solvability. This project explores graph theory, pathfinding, recursion, algorithm design, data structures, and grid-based rendering, focusing on logic validation and procedural content generation.


## 📖 Maze Generator Module Documentation
How to Instantiate and Use
```python
from mazegen import MazeGenerator

# Create the generator
generator = MazeGenerator(width=20, height=10)

# Generate the structure and solve it
generator.generate()
```
### Custom Parameters
You can pass the following parameters to the constructor:

width (int): Number of columns.

height (int): Number of rows.

seed (int, optional): Random seed for reproducible mazes.

perfect (bool): If True, generates a perfect maze (no loops).

### Accessing Data
Structure: Access the grid via generator.grid. It returns a 2D list of Cell objects.

Solution: Access the path from origin to final via generator.solution.