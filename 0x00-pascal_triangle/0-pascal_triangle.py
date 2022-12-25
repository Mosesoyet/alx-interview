#!/usr/bin/python3
"""
A program to print pascal triangle till n'th number
"""

def pascal_triangle(n):
    """
    print n'th number of pascal triangle
    if n <= 0:
    return 0;
    """
    res = []
    for i in range(n):
        if (n <= 0) : return []
        temp_list = []
        for j in range(i):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(res[i-1][j-1] + res[i-1][j])
        res.append(temp_list)
    return res
