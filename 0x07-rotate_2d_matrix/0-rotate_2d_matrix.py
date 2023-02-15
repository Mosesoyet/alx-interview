#!/usr/bin/python3
""" 
Rotate 2d Matrix modules
"""


def rotate_2d_matrix(matrix):
    """ Print 2d matrix and rotates it to 90 deg
    """
    matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
    return None
