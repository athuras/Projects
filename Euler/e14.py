#!/usr/bin/env python
from collections import Counter


def E14(n):
    '''What starting number x < n, produces the logest sequence according to:
    n -> n / 2 if n % 2 == 0
    n -> 3n + 1 if n % 2 != 0
    '''
    def seq_len(x, memo=Counter()):
        '''Updates memo with terms from the sequence started by x'''
        # This could be streamlined a little to reduce dict lookups, but
        # 'key in dict' is so sweet.
        seq = []
        memo[1] = 1
        while x != 1:  # This may be an infinite loop (Collatz Problem)
            seq.append(x)
            if x in memo:
                break
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
        t = 1
        if x in memo:
            t = memo[x] + 1
        while len(seq) != 0:
            memo[seq.pop()] = t
            t += 1

    memo = Counter()
    for i in range(1, n + 1):
        seq_len(i, memo)
    return memo.most_common(1)[0]







