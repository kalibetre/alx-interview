#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix


def test_rotate_3x3_matrix():
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    rotate_2d_matrix(input_matrix)
    assert input_matrix == expected_output


def test_rotate_4x4_matrix():
    input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                    [13, 14, 15, 16]]
    expected_output = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3],
                       [16, 12, 8, 4]]
    rotate_2d_matrix(input_matrix)
    assert input_matrix == expected_output


if __name__ == "__main__":
    test_rotate_3x3_matrix()
    test_rotate_4x4_matrix()
    print("OK!")
