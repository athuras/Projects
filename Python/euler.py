# Add All the natural numbers below 1000 that are multiples of 3 and 5
from itertools import count

def euler1(n=1000,factors=[3,5]): # using list comprehension
	return sum( x for x in generateMultiples(n, factors) )

# first attempt at a generator object
def generateMultiples(n=1,factors=[1]):
	multiples = []
	for i in count():
		if 0 < n < i:
			return
		multiple = False
		for j in multiples:
			if i % j == 0:
				multiple = True
				break
		if multiple:
			multiples.append(i)
			yield i

