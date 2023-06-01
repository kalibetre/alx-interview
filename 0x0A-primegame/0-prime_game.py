#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    """
    checks if a number is prime
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def next_prime(min, max):
    """
    returns the lowest prime next to min but not greater than or equal to max
    """
    if min is None:
        return 2 if max >= 2 else None

    for i in range(min + 1, max + 1):
        if is_prime(i):
            return i
    return None


def remove_multiples(picks, checks):
    """
    removes multiples of the numbers in checks from picks
    """
    return list(
        filter(
            lambda x: not any([x % n == 0 for n in checks]),
            picks,
        ))


def run_game(n):
    """
    runs the game for a particular number
    """
    maria_picks = []
    ben_picks = []
    remaining_picks = list(range(1, n + 1))

    current_pick = None
    while (True):
        current_pick = next_prime(current_pick, n)
        if current_pick is None:
            return 'B'

        maria_picks.append(current_pick)
        remaining_picks = remove_multiples(remaining_picks, maria_picks)

        current_pick = next_prime(current_pick, n)
        if current_pick is None:
            return 'M'
        ben_picks.append(current_pick)
        remaining_picks = remove_multiples(remaining_picks, ben_picks)


def isWinner(x, nums):
    """
    runs the game for the specified rounds in nums array
    """

    invalid_nums = type(nums) is not list or len(nums) == 0 or any(
        type(n) is not int or n < 0 for n in nums)
    invalid_x = type(x) is not int or x != len(nums)
    if invalid_nums or invalid_x:
        return None

    stats = {'B': 0, 'M': 0}
    for n in nums:
        stats[run_game(n)] += 1

    if stats['M'] == stats['B']:
        return None

    return 'Maria' if stats['M'] > stats['B'] else 'Ben'
