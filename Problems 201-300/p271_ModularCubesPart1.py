# For a positive number n, define S(n) as the sum of the integers x,
# for which 1<x<n and x^3≡1 mod n.
# 
# When n=91, there are 8 possible values for x, namely:
# 9, 16, 22, 29, 53, 74, 79, 81.
# Thus, S(91)=9+16+22+29+53+74+79+81=363.
# 
# Find S(13082761331670030).

# THEORY:
# 
# n = 13082761331670030 is the product of all primes up to 43.
# x^3 = 1 mod n if and only if x^3 = 1 mod p for all primes p which divide n.
# 
# For each prime p:
# Assume we already have a solution s for which s^3=1 mod n, and x = 1 mod p.
# Then for each k such that k^3 = 1 mod p:
# Let s' = s * (n/p)^(p-1) * (k-1) + 1.
# Then s' = s mod p' for every p' not equal to p,
# and s' = k mod p.
# 
# The solutions can be found by iterating through the p's in this manner,
# constructing a tree of solutions.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    n = 13082761331670030
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    old_sols = [1]
    for p in primes:
        sols = old_sols[:]  # 1^3=1 mod p always
        # Find all k for which k^3=1 mod p
        for k in range(2, p):
            if pow(k, 3, p) == 1:
                for s in old_sols:
                    sols.append((s * (pow(n // p, p-1, n) * (k-1) + 1)) % n)
        old_sols = sols
    return sum(old_sols) - 1  # problem specifies solutions greater than 1

if __name__ == "__main__":
    start = time()
    peresult(271, solve(), time() - start)
