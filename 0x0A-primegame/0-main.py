#!/usr/bin/python3
"""
Main file for testing
"""
isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(0, [])))
print("Winner: {}".format(isWinner(1, [10000, 1])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
