#!/usr/bin/env python
from aux import gen_Fib

# This can be made more efficient if the goal is to always have the base as 2
# (like the problem states) however, for the sake of generalisation, and fun
# I'll allow any base.
def E2(N, base):
    '''Find the sum of all Fibonacci terms that are multiples of base'''
    s = 0
    for term in gen_Fib(N):
        if term % base == 0:
            s += term
        else:
            continue
    return s
