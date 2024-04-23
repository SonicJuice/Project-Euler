"""
Pentagon Numbers
------------------
Pentagonal numbers are generated by: Pn = n(3n − 1) / 2. P4 + P7 = 22 + 70 = 92 = P8; 
however, their difference, 70 − 22 = 48, is not pentagonal.

Using the pair of pentagonals, Pj and Pk, for which their sum and difference are 
pentagonal, and D = |Pk − Pj| is minimised, calculate D.
"""

""" 1). If n is pentagonal, there exists k such that: (isqrt(24n + 1) + 1) // 6.
Thus, n is only pentagonal if it's the kth pentagonal. 

2). If p[j], p[k] are two pentagonals where j < k: p[k] - p[j] == k(3k - 1) / 2 
- j * (3j - 1) / 2 == p[k - j] + 3j * (k - j).

3). Only pairs (j, k) where the differences are a pentagonal p[t] are needed. 
Setting s = k - j gives: p[t] == p[s] + 3j * s. It thus suffices to only consider 
pairs (s, t), where s < t, for which p[t] - p[s] is a multiple of 3s. These 
automatically yield j and k such that p[k] - p[j] == p[t], leaving the need to only 
check p[j] + p[k] for pentagonality.

4a). As the minimum p[t] with the above properties is needed, consider each s < t 
before moving on to t + 1. Given the cost of calculating (p[t] - p[s]) % (3s), 
first screen candidate s values in view of the following.

4b). For all non-negative integers n: (p[n] - n) % 3 == (n(3n - 3) / 2) % 3 == 
0. Thus, if (p[t] - p[s]) % (3s) == 0, it must be had that (t - s) % 3 == 0

4c). If (p[t] - p[s]) % (3s) == 0: (p[t] - p[s]) % s == 0 => 2 * p[t] % s == 0 """

import math
import itertools

def _nth_pentagonal(n):
    return n * (3 * n - 1) // 2

def _is_pentagonal(n):
    k = (math.isqrt(24 * n + 1) + 1) // 6
    return _nth_pentagonal(k) == n

def pentagonal_number():
    p = {}
    """ itertools.count() creates an iterator that counts up or down infinitely, 
    starting at 0 and incrementing by 1 by default. """
    for t in itertools.count():
        p[t] = _nth_pentagonal(t)
        double_p_t = 2 * p[t]
        for s in range(t - 3, 0, -3):
            if not double_p_t % s and not (p[t] - p[s]) % (3 * s):
                j = (p[t] - p[s]) // (3 * s)
                if _is_pentagonal(p[t] + 2 * _nth_pentagonal(j)):
                    return p[t]

if __name__ == "__main__":
    print(pentagonal_number())
