#!/usr/bin/env python3
""" 
Rotate 2d Matrix modules
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """ Print 2d matrix and rotates it to 90 deg
    """
    new_list = []
    for i in zip(*matrix):
        new_list.append(i[::-1])
        matrix[:] = new_list
