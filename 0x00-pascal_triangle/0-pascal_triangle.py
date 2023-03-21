def pascal_triangle(n):
    """generates a pascal triangle

    Args:
        n (int): number of rows

    Returns:
        list(list(int)): list of lists of integers
    """
    triangle = list()
    if n > 0:
        for i in range(n):
            row = [1]
            for j in range(1, i + 1):
                row.append(triangle[i - 1][j - 1] +
                           triangle[i - 1][j] if i != j else 1)
            triangle.append(row)
    return triangle
