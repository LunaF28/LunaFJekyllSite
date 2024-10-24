---
layout: default
modal-id: "portfolio-5"
title: "Python Maze Creator and Solver"
date: 2023-01-01
img: submarine.png
alt: "Submarine Image"
project-date: 2024-10-22 1:00:00 -0400
client: HZ
category: Python Coding
description: "This is a Python 3 program that creates and (optionally) solves a perfect maze"
---

## Maze Generator and Solver

This Python program generates a **perfect maze**, where each tile has only one possible path from itself to any other tile. Here's an overview of its functionality:

### Key Features
- **Maze Generation**:
  - The maze is created with the requested length and width.
  - The **start tile** (green) is always the bottom left tile.
  - The **end tile** (red) is set to be the farthest tile from the start.
  - The **near solution** (blue) is the closest dead end that deviates from the main path.

- **Maze Solving** (Optional):
  - A **red line** is drawn from the start to the near solution.
  - The line then turns **green** to lead to the true solution (the end tile).

### Visualization
1. The maze starts as a **grid of tiles**.
2. As the maze is generated, tiles turn **pink**, representing the path that has been explored.
   - When the creator hits a **dead end**, it backtracks and pink tiles are removed.
3. During solving, the maze turns **light blue**, indicating progress through a depth-first search:
   - The solver follows a single path until reaching a dead end.
   - Upon reaching a split in the path, a **random direction** is chosen from unexplored options.

### Pathfinding
- The program stores all paths from the start to dead ends.
- It compares the lengths of these paths to find:
  - The **longest path** (which becomes the true solution).
  - The **shortest path** (which becomes the near solution).
  
- The paths are visualized with lines:
  - **Red line**: From the start to the near solution.
  - **Green line**: From the deviation in the path to reach the near solution to the end.

### Development Info
- Written in **Python 3.11.5**.
- Recommended to run in **IDLE**.

### Download
- [Download the maze maker+solver here!](programs/maze-with-actual-docs.py)

### Example Maze
![Created and Solved Maze](img/portfolio/maze.png)

