# Let B(n)=∏_{k=0}^n Binom(n,k), a product of binomial coefficients.
# For example, B(5)=1×5×10×10×5×1=2500.
#
# Let D(n)=∑_{d|B(n)} d, the sum of the divisors of B(n).
# For example, the divisors of B(5) are 1, 2, 4, 5, 10, 20, 25, 50, 100, 125,
# 250, 500, 625, 1250 and 2500, so D(5) = 1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 +
# 100 + 125 + 250 + 500 + 625 + 1250 + 2500 = 5467.
#
# Let S(n)=∑_{k=1}^n D(k).
# You are given S(5)=5736, S(10)=141740594713218418
# and S(100) mod 1000000007=332792866.
#
# Find S(20000) mod 1000000007.

# THEORY:
#
# B(n) = (n!)^(n+1) / (0! * 1! * ... * n!)^2
# Doing the math, this works out to the recursive formula
# B(n) = B(n-1) * n^n / n!.
#
# If x and y are prime, the divisors of x^a * y^b sum to
# (1 + x + ... + x^a) * (1 + y + ... + y^b)
# = (x^(a+1) - 1) / (x - 1) * (y^(b+1) - 1) / (y - 1).
#
# This program keeps track of the prime factors of n! and B(n) as n increases,
# as well as D(n).
# For each n, calculate the prime factors, and update n! and B(n) accordingly.
# While updating B(n), update D(n).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 20000):
    mod = 1000000007
    primes = primesbelow(cap + 1)
    bf = [0 for p in primes]  # Factors of B(n)
    ff = [0 for p in primes]  # Factors of n!
    result = 0
    for n in range(1, cap + 1):
        D = 1
        N = n  # A copy to determine the prime factors
        for i in range(len(primes)):
            p = primes[i]
            exp = 0
            while N % p == 0:
                exp += 1
                N //= p
            ff[i] += exp
            if ff[i] == 0:
                break
            bf[i] += exp * n - ff[i]
            D *= pow(p, bf[i] + 1, mod) - 1
            D *= pow(p - 1, mod - 2, mod)
            D %= mod
        result += D
        result %= mod
    return result

if __name__ == "__main__":
    start = time()
    peresult(650, solve(), time() - start)
