#!/usr/bin/env python
from aux import list2i, i2list, gen_PrimeFactors, intlen
from collections import Counter


def gen_palindromeList():
    '''Generate a list of palindromes . . .'''
    def pfromi(x):
        l, r = i2list(x), i2list(x)
        r.reverse()
        l.extend(r)
        return list2i(l)

    x = 999
    while x > 100:
        p = pfromi(x)
        x -= 1
        if p >= 999**2:
            continue
        yield p
    return


def greatestPair(factors):
    '''Reduce to A * B, in a novel way'''
    def switch():
        while True:
            yield True
            yield False
    ff = switch()
    z = ff.next()
    x = [1, 1]
    Q = factors.most_common()
    Q.reverse()
    for k, v in Q:
        while v != 0:
            x[z] *= k
            v -= 1
            if x[z] > x[not z]:
                z = ff.next()
    return x


# I had some fun with this one, mostly just to explore prime factorization
# This is needlessly complicated for the requirements of this task
# Rather than exhaustively checking all products of A, and B (like the sggested
# Euler solution), this takes the problem backwards, by generating some
# possible large palindromes, then checking whether they can be factored into
# A * B = p.
def E4A():
    '''Return the largest palindrome P, where p = A * B, and A, B > 100'''
    ps = gen_palindromeList()
    for n in ps:
        pCount = Counter()
        for p in gen_PrimeFactors(n):
            pCount.update(p)
        A, B = greatestPair(pCount)
        if intlen(A) == 3 and intlen(B) == 3:
            return n
