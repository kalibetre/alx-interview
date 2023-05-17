#!/usr/bin/python3
"""
Test 0x08 Coin Change Problem
"""


def memoized_make_change_rec(func):
    """Memoization decorator for make_change_rec function
    """
    memory = {}

    def wrapped(coins, total, org_total):
        """Wrapper function for make_change_rec function"""
        if total in memory:
            return memory[total]
        result = func(coins, total, org_total)
        if total == org_total:
            memory.clear()
            return result
        memory[total] = result
        return memory[total]

    return wrapped


@memoized_make_change_rec
def make_change_rec(coins, total, org_total):
    """Given coins and a total it determines and returns the
    fewest possible number of coins needed to meet the given
    amount.

    Returns:
        - fewest number of coins if total can be met
        - 0 if total is 0 or less
        - -1 if total cannot be met by any number of coins
    """
    if total == 0:
        return 0

    possible_coins = list(filter(lambda c: c <= total, coins))
    if len(possible_coins) == 0:
        return -1

    results = []
    for coin in possible_coins:
        result = make_change_rec(possible_coins, total - coin, org_total)
        results.append(result)

    min_change = min(results)
    return min_change + 1 if min_change >= 0 else -1


def makeChange(coins, total):
    """Calls make_change_rec function with the original total as a parameter
    to clear the memory cache.

    Returns:
        - fewest number of coins if total can be met
        - 0 if total is 0 or less
        - -1 if total cannot be met by any number of coins
    """
    return make_change_rec(coins, total, total)
