#!/usr/bin/python3
"""
Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island given by the gird representation
    """
    perimeter = 0
    height = len(grid)
    width = len(grid[0])

    next_cells = []
    visited_cells = []

    for i in range(1, height - 2):
        if (len(next_cells)):
            break
        for j in range(1, width - 2):
            if (grid[i][j] == 0):
                continue
            else:
                next_cells.append((i, j))
                break

    if (len(next_cells) == 0):
        return perimeter

    while (len(next_cells) > 0):
        cell = next_cells.pop()

        left = (cell[0], cell[1] - 1)
        top = (cell[0] - 1, cell[1])
        right = (cell[0], cell[1] + 1)
        bottom = (cell[0] + 1, cell[1])

        if (grid[left[0]][left[1]] == 0):
            perimeter += 1
        elif (left not in visited_cells):
            next_cells.append(left)

        if (grid[top[0]][top[1]] == 0):
            perimeter += 1
        elif (top not in visited_cells):
            next_cells.append(top)

        if (grid[right[0]][right[1]] == 0):
            perimeter += 1
        elif (right not in visited_cells):
            next_cells.append(right)

        if (grid[bottom[0]][bottom[1]] == 0):
            perimeter += 1
        elif (bottom not in visited_cells):
            next_cells.append(bottom)

        visited_cells.append(cell)

    return perimeter
