#!/usr/bin/env python
from aux import gen_Primes

def E10(n):
    '''Return the sum of all primes below n'''
    s, primes = 0, gen_Primes()
    for p in primes:
        if p < n:
            s += p
        else:
            return s
