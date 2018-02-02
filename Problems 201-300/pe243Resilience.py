# A positive fraction whose numerator is less than its denominator is
# called a proper fraction.
# For any denominator, d, there will be d−1 proper fractions; for example,
# with d = 12:
# 1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.
# 
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the
# ratio of its proper fractions that are resilient; for example, R(12) = 4/11.
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10.
# 
# Find the smallest denominator d, having a resilience R(d) < 15499/94744.

# THEORY:
# 
# If phi(n) is Euler's totient function, then R(d) = phi(d) / (d - 1).
# If d = p1 * p2 * p3 * ... * pk, with all primes p distinct,
# then R(d) = ((p1 - 1) * ... * (pk - 1)) / ((p1 * ... * pk) - 1).
# Multiplying d by a prime p that it's already divisible by results in the
# numerator and the left half of the denominator both being multiplied by p.
# 
# This means that to minimize R(d), d should first be set equal to a product
# of distinct primes D, and then be set equal to multiples of D until the -1
# in the denominator ceases to be significant.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 15499/94744):
    start = time()
    primes = primesbelow(100)  # Safe overestimate
    numerator = 1
    n = 1
    for p in primes:
        if (numerator * (p - 1)) / (n * p - 1) > cap:
            numerator *= p - 1
            n *= p
        else:
            for mult in range(1, p):
                if (numerator * mult) / (n * mult - 1) < cap:
                    result = n * mult
                    break
            break
    else:  # Loop fell through. Primes list wasn't long enough
        raise RuntimeError("Primes list in code too short. Edit and extend")
    peresult(243, result, time() - start)

if __name__ == "__main__":
    solve()
