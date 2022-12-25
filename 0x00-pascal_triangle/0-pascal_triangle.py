#!/usr/bin/python3
"""
A program to print pascal triangle till n'th number
"""

def pascal_triangle(n):
    """
    print n'th number of pascal triangle
    >>> if n <= 0:
    >>>     return 0;
    """
    if n <= 0:
        return []
    for i in range(n):
        print(' '*(n-1), end="")
        print(' '.join(map(str, str(11**i))))

pascal_triangle(5)