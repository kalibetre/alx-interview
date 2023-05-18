#!/usr/bin/python3
"""
Test 0x08 Coin Change Problem
"""


def makeChange(coins, total):
    """makeChange with dynamic programming implementation

    Returns:
        - fewest number of coins if total can be met
        - 0 if total is 0 or less
        - -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    memory = [0] + [float('inf')] * total

    for coin in coins:
        for num in range(coin, total + 1):
            if coin <= num:
                memory[num] = min(memory[num], memory[num - coin] + 1)

    return memory[total] if memory[total] != float('inf') else -1
