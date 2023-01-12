#!/usr/bin/python3
"""
Minimum Operation's module
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly n H x-tors
    """
    pasted_chars == 1 # No of x-tors in file
    clipboard = 0 # How many H's copied
    counter = 0 # Operations counter

    while pasted_chars < n:
        # If nothing is copied
        if clipboard == 0:
            # Copy  *
            clipboard = pasted_chars
            # counter ++
            counter += 1

        # If haven't posted yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chars
        if remaining < clipboard:
            return 0

        # if can't be divided
        if remaining % pasted_chars != 0:
            counter += 1
        else:
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            counter += 2

    # if got the desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
