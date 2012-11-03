import itertools
from math import log10, log, floor
from numpy.random import random_integers
# Utility methods for use with project euler.

# Generators
def pairwiseCmp(fct):
    '''Generate the unique cartesian product terms of a sequence
    for [A, B, C] we get (A*B, A*C, B*C)'''
    for i, x in enumerate(fct):
        for j in fct[i + 1:]:
            yield x * j


def gen_Multiples(n,factors):
    '''Generate multiples of a group of factors'''
    for i in itertools.count():
		if 0 < n < i:
			return
		for j in factors:
			if j % i == 0:
				yield i
				break


def gen_Primes(n=1000000):
    '''Prime Number Generator using sieve of Eratosthenes'''
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
	    p = D.pop(q, None)
	    if p is None:
		    D[q*q] = q
		    yield q
	    else:
		    x = p + q
		    while x in D or not (x&1):
			    x += p
		    D[x] = p

def gen_PrimeFactors(x):
    '''Incrementally return a map of a prime factor, to its weight in x

    i.e. all iters of gen_PrimeFactors(125) = {5:2}'''
    ps = gen_Primes()
    while x > 1:
        p = ps.next()
        if x % p == 0:
            i = 0
            while x % p == 0:
                i += 1
                x /= p
            yield {p: i}
    return


def gen_fib(n, a0=1, a1=2):
    '''Generate Numbers in the Fibonacci Sequence'''
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

# Utility
def ireduce(f, iterable, init=None):
    '''efficient version of reduce'''
    if init is None:
        iterable = iter(iterable)
        curr = iterable.next()
    else:
        curr = init
    for x in iterable:
        curr = f(curr, x)
        yield curr

def intlen(x, incl_neg=False):
    '''The number of digits required to represent an integer'''
    if x > 0:
        return int(log10(x)) + 1
    elif x == 0:
        return 1
    else:
        return int(log10(-x) + 1) + incl_neg

def isRMPrime(n, k=8):
    '''Rabin-Miller probabalistic primality test. Error O(4**-k)'''
    if n in set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]):
        return True
    if n % 2 == 0:
        return False
    s = int(floor(log(n-1, 2)))
    d = (n - 1) / s
    for i in range(k):
        a = random_integers(2, n - 2)
        x = (a ** d ) % n
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
        if short == True:
            return False
    return True

def list2i(x):
    '''Convert a list of integers into a single int

    i.e. list2i([1,2,3]) = 123'''
    y = 0
    for i, v in enumerate(x):
        y += v * 10**i
    return y

def i2list(x):
    '''Convert an integer into a list of single-digit integers

    i.e. i2list(123) = [1, 2, 3]'''
    return [int[z] for z in str(x)]
