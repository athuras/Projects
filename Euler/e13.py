#!/usr/bin/env python
import numpy as np


def E13(fn):
    '''Find the first 10 digits of the sum of 100, 50digit numbers'''
    # enter numpy arrays.
    x = []
    for line in open(fn, 'r'):  # this could be done better ...
        x.append(line.rstrip('\n'))
    z = np.array([int(p) for q in x for p in q]).reshape(100,50)  # heavy lifting
    y = list(z.sum(axis=0))
    for i in range(len(y) - 1, 0, -1):
        y[i - 1] += int(y[i]) / 10
        y[i] %= 10
    z = ''
    for i in range(len(y)):
        z += str(y[i])
        if len(z) > 10:
            return z[:10]
    return z
