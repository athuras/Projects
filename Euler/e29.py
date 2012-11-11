#!/usr/bin/env python


def E29(x, y):
    '''How many distint terms are in the sequenc a^b for a, b in [x, y]'''
    # Simple brute force application works comfortably for |[x,y]| < 1000
    items = (i**j for i in xrange(x, y + 1) for j in xrange(x, y + 1))
    sequence = set(items)
    return len(sequence)
