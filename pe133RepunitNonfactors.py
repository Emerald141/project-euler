# A number consisting entirely of ones is called a repunit.
# We shall define R(k) to be a repunit of length k;
# for example, R(6) = 111111.
#
# Let us consider repunits of the form R(10^n).
#
# Although R(10), R(100), or R(1000) are not divisible by 17,
# R(10000) is divisible by 17. Yet there is no value of n for
# which R(10^n) will divide by 19. In fact, it is remarkable that
# 11, 17, 41, and 73 are the only four primes below one-hundred
# that can be a factor of R(10^n).
#
# Find the sum of all the primes below one-hundred thousand that
# will never be a factor of R(10^n).

# THEORY:
# 
# R(k) = (10^k - 1) / 9
# 
# For prime p > 5, let s be the smallest natural number such that
# 10^s = 1 mod p. Because 10^(p-1) = p mod p, s divides p-1.
# Because p divides 10^s - 1, p divides R(s).
# 
# Consider A = ks + d, for positive k and 0 <= d < p. Then:
# R(A) = (10^A - 1). 9
# = (10^(ks + d) - 10^(ks) + 10^(ks) - 10^((k-1)s) + ... + 10^s - 1) / 9
# = 10^(ks) R(d) + Σ_{i=0}^{k-1} 10^(is) R(s)
# = (nondivisor of p) * (divisor of p iff d = 0) + (divisor of p)
# = (divisor of p iff d = 0)
# 
# Therefore p divides some R(10^n) if and only if
# no primes except 2 and 5 divide s.

from time import time
from peresult import peresult
from primefns import primesbelow

def pe133(cap):
    start = time()
    result = 0
    primes = primesbelow(cap)
    primes.pop(1)  # 3 returns a false positive for the test below,
                   # because 3 divides 10^2 - 1, but not R(2)
    for p in primes:
        x = p - 1
        while x % 2 == 0:
            x //= 2
        while x % 5 == 0:
            x //= 5
        if pow(10, (p - 1) // x, p) != 1:
            result += p
    result += 3  # Need to add 3 back in
    peresult(133, result, time() - start)

if __name__ == "__main__":
    pe133(100000)
