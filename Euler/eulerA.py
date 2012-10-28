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


def gen_fib(n, a0=1, a1=2):
    a0, a1 = 1, 2
    z = 0
    if n > 1:
        yield 1
    if n > 2:
        yield 2
    while True:
        z = a0 + a1
        a0, a1 = a1, z
        if z < n:
            yield z
        else:
            return


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

# This can be made slightly more efficient if the goal is to always have the
# base as even, however for the sake of allowing any base to be used the
# mod-test is kept, and we don't skip any fibonacci numbers.
def euler2(N, base):  # First attempt
    s = 0
    for term in gen_fib(N):
        if term % base == 0:
            s += term
        else:
            continue
    return s
