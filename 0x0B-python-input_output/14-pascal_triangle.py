#!/usr/bin/python3
"""Define class"""


def pascal_triangle(n):
    """Returns list of lists of integers representing Pascal's triangle"""
    if n <= 0:
        return []

    big = [[1]]
    for i in range(1, n):
        sm = [1]
        for j in range(1, i):
            sm.append(big[i-1][j-1] + big[i-1][j])
        sm.append(1)
        big.append(sm)

    return big
