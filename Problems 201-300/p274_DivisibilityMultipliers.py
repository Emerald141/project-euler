# For each integer p > 1 coprime to 10 there is a positive divisibility
# multiplier m < p which preserves divisibility by p for the following
# function on any positive integer, n:
# 
# f(n) = (all but the last digit of n) + (the last digit of n) * m
# 
# That is, if m is the divisibility multiplier for p, then f(n) is divisible
# by p if and only if n is divisible by p.
# 
# (When n is much larger than p, f(n) will be less than n and repeated
# application of f provides a multiplicative divisibility test for p.)
# 
# For example, the divisibility multiplier for 113 is 34.
# 
# f(76275) = 7627 + 5 * 34 = 7797: 76275 and 7797 are both divisible by 113
# f(12345) = 1234 + 5 * 34 = 1404: 12345 and 1404 are both not divisible by 113
# 
# The sum of the divisibility multipliers for the primes that are coprime to 10
# and less than 1000 is 39517.
# What is the sum of the divisibility multipliers for the primes that are
# coprime to 10 and less than 10^7?

# THEORY:
# 
# For any prime p coprime to 10:
# Let m be the divisibility multiplier for m, and let s be any 1-digit number.
# Then 10n + s = 0 mod p if and only if n + ms = 0 mod p.
# The latter equation is equivalent to 10n + 10ms = 0 mod p.
# Subtracting the first equation from the last yields (10m - 1)s = 0 mod p.
# Because s can be any number from 0 to 9, this means 10m - 1 = 0 mod p.
# That is, if m is the modular inverse of 10 mod p.
# Because p is prime, m = 10^(p-2) mod p.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 10 ** 7):
    primes = primesbelow(cap)
    result = 1  # divisibility multiplier for 3
    for p in primes[3:]:  # skipping 2, 3, and 5
        result += pow(10, p - 2, p)
    return result

if __name__ == "__main__":
    start = time()
    peresult(274, solve(), time() - start)
