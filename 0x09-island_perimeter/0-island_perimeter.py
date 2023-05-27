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

    for i in range(0, height):
        if (len(next_cells)):
            break
        for j in range(0, width):
            if (grid[i][j] == 0):
                continue
            else:
                next_cells.append((i, j))
                break

    if (len(next_cells) == 0):
        return perimeter

    while (len(next_cells) > 0):
        cell = next_cells.pop()
        if cell in visited_cells:
            continue

        left = (cell[0], cell[1] - 1)
        top = (cell[0] - 1, cell[1])
        right = (cell[0], cell[1] + 1)
        bottom = (cell[0] + 1, cell[1])

        if (left[1] < 0 or grid[left[0]][left[1]] == 0):
            perimeter += 1
        else:
            next_cells.append(left)

        if (top[0] < 0 or grid[top[0]][top[1]] == 0):
            perimeter += 1
        else:
            next_cells.append(top)

        if (right[1] >= width or grid[right[0]][right[1]] == 0):
            perimeter += 1
        else:
            next_cells.append(right)

        if (bottom[0] >= height or grid[bottom[0]][bottom[1]] == 0):
            perimeter += 1
        else:
            next_cells.append(bottom)

        visited_cells.append(cell)

    return perimeter
