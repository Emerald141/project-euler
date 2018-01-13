# Consider the numbers 15, 16 and 18:
# 15=3×5 and 3+5=8.
# 16=2×2×2×2 and 2+2+2+2=8.
# 18=2×3×3 and 2+3+3=8.
# 15, 16 and 18 are the only numbers that have 8 as sum of the prime factors
# (counted with multiplicity).
# 
# We define S(k) to be the sum of all numbers n where the sum of the
# prime factors (with multiplicity) of n is k.
# Hence S(8)=15+16+18=49.
# Other examples: S(1)=0, S(2)=2, S(3)=3, S(5)=5+6=11.
# 
# The Fibonacci sequence is F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, ...
# Find the last nine digits of ∑_(k=2)^24 S(F_k).

# THEORY:
#
# Let S(k, p) be the sum of all numbers n where the sum of the prime factors
# (with multiplicity) of n is k, and n has no prime factors larger than p.
#
# If k is even, S(k, 2) = 2 ^ (k / 2). If k is odd, S(k, 2) = 0.
#
# For p > 2, let p' be the prime immediately preceding p.
# If k < p, then S(k, p) = S(k, p').
#
# If k >= p, the sum of all n such that p divides n, no primes larger than p
# divide n, and the prime factors of n sum to k is equal to p * S(k - p, p).
# Therefore S(k, p) = p * S(k - p, p) + S(k, p').
#
# This code runs slower than I'd like; it just barely gets inside the
# 60-second threshold.

from time import time
from peresult import peresult
from primefns import primesbelow

def pe618():
    start = time()
    mod = 10 ** 9
    fibo = [1, 2]
    for x in range(21):  # Last element is 24th fibonacci number
        fibo.append(fibo[-1] + fibo[-2])
    primes = primesbelow(fibo[-1])
    sums = [0 for x in range(fibo[-1] + 1)]  # sums[k] == S(k, p) at end of loop
    sums[0] = 1  # 1 is the only integer whose prime factors sum to 0
    for p in primes:
        for k in range(p, len(sums)):
            sums[k] += p * sums[k - p]
            sums[k] %= mod
    result = 0
    for f in fibo:
        result += sums[f]
    result %= mod
    peresult(618, result, time() - start)

if __name__ == "__main__":
    pe618()
