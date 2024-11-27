#!/usr/bin/python3
"""make change"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of the values of the coins.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed, or -1 if the total cannot be met.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0

    for coin in coins:
        if total >= coin:
            num_coins += total // coin
            total %= coin

        if total == 0:
            break

    return num_coins if total == 0 else -1
