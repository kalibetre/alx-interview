#!/usr/bin/python3
"""
0-minoperations module
"""
import math


def get_largest_factor(n):
    """
    returns the largest factor of a number excluding the number itself
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n // i
    return 1


def minOperations(n):
    """
    returns the minium number of operations required to generate n consecutive
    'H' characters using 'Copy All' and 'paste' operations. If n is impossible
    to achieve returns 0

    Example: for n = 9 the minimum number of operations is 6
    H => Copy All => paste => HH => paste => HHH => Copy All => paste => HHHHHH
    => paste => HHHHHHHHH

    Algorithm Used
    factors of 12 => 1, 2, 3, 4, 6, 12 => largest = 6
    12 / 6 = 2 => HHHHHH => copy all => paste => HHHHHHHHHHHH
    factors of 6 => 1, 2, 3, 6 => largest = 3
    6 / 3 = 2 => HHH => copy all => paste => HHHHHH
    factors of 3 => 1, 3 => largest = 1
    H => copy all => paste => HH => paste => HHH
    """
    if n <= 1:
        return 0
    largest_factor = get_largest_factor(n)
    if largest_factor == 1:
        return n
    return n // largest_factor + minOperations(largest_factor)
