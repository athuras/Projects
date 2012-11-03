#!/usr/bin/env python
from aux import gen_Primes, intlen, isRMPrime
from math import ceil, sqrt
from collections import Counter

# First Attempt:
# Problem: tests for primality, which is expensive, although it does it
# in a really sexy way (check out aux.isRMPrime).
def E3A(n):
    '''Find the largest Prime Factor of n'''
    if isRMPrime(n):
        return n
    p = int(ceil(sqrt(n)))
    while p > 1:
        if p % 2 == 0:
            p = p / floor(log(p, 2))
        if isRMPrime(p):
            return p
        p -= 1
    return 1

# Lets try going Up to sqrt(n), avoid testing for primes by explicitely
# using prime factors. Much more intuitive, makes E3A look hilarious.
# This is why I practice . . .
def E3B(n):
    '''Find the largest Prime Factor of n'''
    ps = gen_Primes()
    p = 0
    while n > 1:
        p = ps.next()
        if n % p == 0:
            while n % p == 0:
                n /= p
    return p
