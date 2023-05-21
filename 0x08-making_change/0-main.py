#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change_rec').makeChange

print(makeChange([1, 4, 5], 8))
print(makeChange([1, 2, 25], 37))
print(makeChange([25, 10, 5, 2, 1], 2147483647))
print(makeChange([1256, 54, 48, 16, 102], 1453))
print(makeChange([4, 5], 7))
