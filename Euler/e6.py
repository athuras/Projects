#!/usr/bin/env python

# trivial
def E6A(n):
    '''Find the difference between the sum of squares, and square of sums'''
    s1, s2 = 0, 0
    for i in range(1, n + 1):
        s1 += i
        s2 += i**2
    return s1**2 - s2
