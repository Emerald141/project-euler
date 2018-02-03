# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes
# for the consecutive values n = 0 to 39. However, when
# n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible
# by 41, and certainly when n = 41, 41^2 + 41 + 41 is
# clearly divisible by 41.
#
# The incredible formula  n^2 − 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values
# n = 0 to 79. The product of the coefficients,
# −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n^2 + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
#
# Find the product of the coefficients, a and b, for the
# quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n = 0.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow, isprime

def solve(cap = 1000):
    b_list = primesbelow(cap)   # b must be prime (consider n = 0)
    longest_streak = 0
    result = 0
    for a in range(-cap, cap + 1):
        for b in b_list:
            n = 1
            while isprime(n ** 2 + a * n + b):
                n += 1
            if n - 1 > longest_streak:
                longest_streak = n - 1
                result = a * b
    return result

if __name__ == "__main__":
    start = time()
    peresult(27, solve(), time() - start)
