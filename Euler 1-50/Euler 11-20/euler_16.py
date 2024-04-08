"""
Power Digit Sum
-----------------
Sum the digits of n^exp.
"""

import math

def power_digits_sum(n, exp):
    power = n ** exp
    digit_sum = 0
    """ math.floor() rounds a number down to the nearest integer; math.log10() 
    returns the base-10 logarithm of a number (i.e. the exponent, how many times to use 
    a given number in a multiplication, to which 10 must be raised to produce n). 
    This is used to represent the length of n. """
    for _ in range(math.floor(1 + exp * math.log10(n))):
        digit_sum += power % 10
        power //= 10
    return digit_sum

if __name__ == "__main__":
    print(power_digits_sum(2, 1000))
