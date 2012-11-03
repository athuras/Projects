#!/usr/bin/env python
from aux import gen_Primes

# Just count up . . .
def E7A(n):
    primes = gen_Primes()
    p = 0
    while n > 0:
        p = primes.next()
        n -= 1
    return p
