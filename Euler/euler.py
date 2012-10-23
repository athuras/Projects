#!/usr/bin/env python
# Euler1. Find the sum of all multiples contained in A, below N
import itertools


def ireduce(f, iterable, init=None):
    if init is None:
        iterable = iter(iterable)
        curr = iterable.next()
    else:
        curr = init
    for x in iterable:
        curr = f(curr, x)
        yield curr


def gen_fib(n):
    a0, a1 = 1, 2
    for i in itertools.count():
        if not 0 <= i < n:
            return
        z = a0 + a1
        a0, a1 = a1, z
        yield z


def euler1(N, factors):  # First Attempt, O(N)

    def gen_multiples(n, factors):
        '''Yield numbers that are multiples of factors'''
        for i in itertools.count():
            if not 0 <= i < n:
                return
            for j in factors:
                if i != 0 and i % j == 0:
                    yield i
                    break

    s = 0
    for i in gen_multiples(N, factors):
        s += i
    return s


def euler1b(N, factors):  # Informed Generalisation, O(1/2*factors^2)

    def sumDivBy(x):
        p = (N - 1) / x
        return x * (p * (p + 1)) / 2

    def pairwiseCmp(fct):
        for i, x in enumerate(fct):
            for j in fct[i + 1:]:
                yield x * j

    result = 0
    for f in factors:
        result += sumDivBy(f)
    for f in pairwiseCmp(factors):
        result -= sumDivBy(f)

    return result
