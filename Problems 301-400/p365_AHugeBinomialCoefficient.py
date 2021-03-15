# The binomial coefficient C(10^18, 10^9) is a number with more than
# 9 billion (9 * 10^9) digits.
# Let M(n,k,m) denote the binomial coefficient C(n,k) mod m.
# Calculate the sum of M(10^18, 10^9, p * q * r) for 1000 < p < q < r < 5000
# and p, q, r prime.

# THEORY:
#
# The first step is to find out C(10^18, 10^9) mod p, for all p.
# Note that C(n, k) = f(n,k) / k!, where f(n,k) is the k'th lower factorial
# of n, i.e. n * (n-1) * (n-2) * ... * (n-k+1).
# If there are more factors of p in f(n,k) than in k!, then C(n,k) mod p = 0.
# Otherwise, node that (p-1)! mod p = -1 mod p, so:
# f(n,k) mod p = (-1)^(k // p) * f(n, k mod p) mod p
# k! mod p     = (-1)^(k // p) * (k mod p)! mod p
# Therefore, C(n, k) = f(n, k mod p) * ((k mod p)!)^(p-2) mod p.
#
# The second step is to use the Chinese Remainder Theorem to combine the
# results from the first step.
# Consider the equations x = a mod m, x = b mod n.
# The Extended Euclidean Algorithm finds s and t such that
# (s * m) + (t * n) = 1.
# Then x = (a * t * n) + (b * s * m).
# Run this first with p and q, then with p * q and r.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

# Find the exponent of p in the prime factorization of n!.
# Not the best name for this function, but I was stymied for a better one.
def fact_prime(n, p):
    result = 0
    power = p
    while power <= n:
        result += n // power
        power *= p
    return result

# Find x and y such that a * x + b * y = 1.
# (precondition that a and b are coprime)
def extended_euclidean(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return (old_s, old_t)

def solve(n = 10 ** 18, k = 10 ** 9):
    primes = [p for p in primesbelow(5000) if p > 1000]
    mods = [0 for p in primes]
    # Step 1: Find C(n, k) mod p for all p
    for i in range(len(primes)):
        p = primes[i]
        # First, find out if the mod is 0
        if fact_prime(n, p) - fact_prime(n - k, p) > fact_prime(k, p):
            print(p, 0)
            continue
        # Since the mod isn't 0, compute it
        mods[i] = 1
        for j in range(1, k % p + 1):
            mods[i] *= (n + 1 - j) * pow(j, p - 2, p)
            mods[i] %= p
        # EXPERIMENTAL
        for mult in range((n // p) * p, n - k, -p):
            temp = mult
            while temp % p == 0:
                temp //= p
            mods[i] *= temp
            mods[i] %= p
        for mult in range(p, k + 1, p):
            temp = mult
            while temp % p == 0:
                temp //= p
            mods[i] *= pow(temp, p - 2, p)
            mods[i] %= p
        print(p, mods[i])
    # Step 2: Find the result over all triples of primes
    result = 0
    for i1 in range(len(primes) - 2):
        print(primes[i1])
        for i2 in range(i1 + 1, len(primes) - 1):
            # Run the Extended Euclidean Algorithm over the first two primes
            p, q = primes[i1], primes[i2]
            (s, t) = extended_euclidean(p, q)
            partial = (mods[i1] * t * q + mods[i2] * s * p) % (p * q)
            for i3 in range(i2 + 1, len(primes)):
                # Run the algorithm again with the third prime
                r = primes[i3]
                (s, t) = extended_euclidean(p * q, r)
                term = (partial * t * r + mods[i3] * s * p * q) % (p * q * r)
                # if mods[i1] and mods[i2] and mods[i3]:
                #     print(partial, p * q, mods[i3], r, term)
                #print('', p, q, r, term, sep='\t')
                result += term
    return result

if __name__ == "__main__":
    start = time()
    peresult(365, solve(), time() - start)
