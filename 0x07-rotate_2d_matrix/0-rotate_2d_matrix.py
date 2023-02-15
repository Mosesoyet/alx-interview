#!/usr/bin/python3
""" 
Rotate 2d Matrix modules
"""


def rotate_2d_matrix(matrix) -> None:
    """ Print 2d matrix and rotates it to 90 deg
    """
    matrix[:] = zip(*matrix[::-1])
