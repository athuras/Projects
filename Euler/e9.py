#!/usr/bin/env python
# For whatever reason, I actually had a really hard time with this one.
# The triplet algorithm below returns a list of triplets, so to answer the
# problem, simply find the product of the singleton e9.triplet(1000)

from aux import fermat_sum_of_squares as fss


def triplet(n):
    '''Find 0 < a < b < c | a + b + c == n, a^2 + b^2 == c^2'''
    # First, lets reduce the problem space, instead of finding a, and b
    # find q = (a + b) | q + c == n. This reduces the scope to O(n^2)
    # Given the above we can assert:
    #   max(q) < 2c, min(q) > 2 (i.e. a, b >= 1)
    #   min(c) > n / 3, max(c) <= n - 3 (0 < a < b >= 2)

    qc = ((q, c) for c in xrange(n - 3, n / 3 - 1, -1)
                 for q in xrange(2 * n - 1, 2, -1)
                     if q + c == n)

    # Using Fermats sum-of-squares assertion, we take only values of c
    # that can be expressed as a sum of squares
    valid = (i for i in qc if fss(i[1]**2))

    # now find a, b given q, c.
    # after some algebra:
    # (n^2)/2 == n*q - a*b
    abc = ((a, b, q[1]) for q in valid
                        for b in xrange(q[0], 1, -1)
                        for a in xrange(min([b - 1, q[0] - b]), 0, -1)
                        if (a + b + q[1] == n
                            and (n**2) / 2 == n * q[0] - a * b
                            and b < q[1]))
    return list(abc)
