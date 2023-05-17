#!/usr/bin/python3
"""
Test 0x08 Coin Change Problem
"""


def makeChange(coins, total):
    """Calls make_change_rec function with the original total as a parameter
    to clear the memory cache.

    Returns:
        - fewest number of coins if total can be met
        - 0 if total is 0 or less
        - -1 if total cannot be met by any number of coins
    """
    memory = [0] + [float('inf')] * total

    for num in range(1, total + 1):
        for coin in coins:
            if coin <= num:
                memory[num] = min(memory[num], memory[num - coin] + 1)

    return memory[total] if memory[total] != float('inf') else -1
