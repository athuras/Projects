#!/usr/bin/env python
from aux import gen_Multiples, pairwiseCmp


def E1A(N, factors):  # First Attempt, O(N)
    '''Return the sum of all factors < N'''
    s = 0
    for i in gen_Multiples(N, factors):
        s += i
    return s

def E1B(N, factors):  # Informed generalisation, O(1/2 * factors**2)
    '''Return the sum of all factors < N'''
    def sumDivBy(x):
        p = (N - 1) / x
        return x * (p * (p + 1)) / 2

    rt = 0
    for f in factors:
        rt += sumDivBy(f)
    for f in pairwiseCmp(factors):
        rt -= sumDivBy(f)
    return rt
