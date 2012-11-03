#!/usr/bin/env python
from aux import gen_PrimeFactors
from collections import Counter

# Again, number theory is key. Here we find the largest prime factor power,
# for the set of all prime factors for all numbers within the range
# then simply combine them to get the answer.
def E5A(n):
    '''Determing the smallest number that is evenly divided by all numbers <= n'''
    def maxMerge(a, b):
        for k, v in b.iteritems():
            if a[k] < v:
                a[k] = v

    master = Counter()
    x = range(2, n + 1)
    for i in x:
        tmp = Counter()
        for p in gen_PrimeFactors(i):
            tmp.update(p)
        maxMerge(master, tmp)

    s = 1
    for k, v in master.iteritems():
        s *= k**v

    return s
