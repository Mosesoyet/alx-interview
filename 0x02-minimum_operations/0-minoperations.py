#!/usr/bin/python3
"""
Minimum Operation's module
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly n H x-tors
    """
    operations = 0
    min_operations = 2

    while n > 1:
        # If character is pasted
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
