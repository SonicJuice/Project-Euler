"""
Quadratic Primes
-------------------
The quadratic formula n^2 − 79n + 1601 produces 80 primes for the consecutive values 0 ≤ 
n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form n^2 + an + b, where |a| < limit and |b| ≤ limit, and 
|n| is modulus n (e.g. |−4| = 4), find the product of the coefficients, a and b 
for the quadratic expression that produces the maximum number of primes for consecutive 
values of n, starting with n = 0.
"""

"""
1). The quadratic n^2 - 79n + 1601 can be expressed as (n - 40)^2 + (n - 40) + 41. 
This shows that if p(n) generates primes for 0 ≤ n ≤ L, p(L - n) also does for the 
same range.

2). Deriving the transformation equation gives p(L - n) = n^2 + an + b, where a = 
-(2L + 1) and b = L^2 + L + 41

3). 163 is the largest Heegner number (square free positive integer d such that the 
ring of algebraic integers Q[sqrt(-d)] forms a unique factorization domain, where every 
non-zero, non-unit element can be uniquely factored into a product of prime elements).
"""

def quadratic_primes(limit):
    """ since Q[sqrt(−163)] is a UFD, every prime generated by the polynomial can be 
    uniquely factored, ensuring that no additional prime factors appear unexpectedly. """
    L = int(0.5 * ((4 * limit - 163) ** 0.5 - 1))
    return (L ** 2 + L + 41) * (-(2 * L + 1))

if __name__ == "__main__":
    print(quadratic_primes(1000))
