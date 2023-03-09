#!/usr/bin/python3
""" Prime Game
"""


def isWinner(x, nums):
    """ x is the number of rounds and nums is an array of n
    """
    if x < 1 or not nums:
        return None
    maria_win = 0
    ben_win = 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] == False
    for i, isprime in enumerate(primes, 1):
        if i == 1 or not isprime:
            continue
        for j in range(i + i, n + 1, 1):
            primes[j - 1] = False
    for _, n in zip(range(x, nums)):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_win += primes_count % 2 == 0
        maria_win += primes_count % 2 == 1
    if ben_win == maria_win:
        return None
    return 'Maria' if maria_win > ben_win else 'Ben'
