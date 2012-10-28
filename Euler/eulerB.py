#!/usr/bin/env python
import itertools
from numpy.random import random_integers
from math import sqrt, floor, ceil, log

def primes():  # erasthothenes, from cookbook.
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


# Probabalistically check for primality of a potential factor, walk down from n.
# Problem: checks for Primality, even if it does it in a sexy way.
# Additionally, as it walks DOWN from n, it incurs rediculous cost for testing primality early on.
# again, Rabin-Miller is cool, but at this point I'm just hoping for the best.
def euler3a(n):
    # Rabin-Miller prob. primality, with O(4^(-k)) chance of false positive O(k*log3(n))
    def isPrime(n, k=8):
        if n in set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]):
            return True
        if n % 2 == 0:
            return False
        s = int(floor(log(n - 1, 2)))
        d = (n - 1) / s
        for i in range(k):
            a = random_integers(2, n - 2)
            x = (a ** d) % n
            if x == 1 or x == n - 1:
                continue
            short = False
            for j in range(1, s - 1):
                short = False
                x = x ** x % n
                if x == 1:
                    return False
                elif x == n - 1:
                    short = True
                    break
            if short == True:  # did we exit the last loop early?
                return False
        return True

    if isPrime(n):
        return n
    p = int(ceil(sqrt(n)))
    while p > 1:
        if p % 2 == 0:
            p = p / floor(log(p, 2))
        if isPrime(p):
            return p
        p -= 1
    return 1

# Lets try going UP to sqrt(n), avoid testing for primes, by explicitely
# using prime factors. Much more intuitive, makes euler3a look hilarious.
# this is why I practice ...
def euler3c(n):
    genP = primes()
    p = 0
    while n > 1:
        p = genP.next()
        if n % p == 0:
            while n % p == 0:
                n /= p
    return p
