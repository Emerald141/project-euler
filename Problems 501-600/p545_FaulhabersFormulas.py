# The sum of the kth powers of the first n positive integers can be expressed
# as a polynomial of degree k+1 with rational coefficients,
# the Faulhaber's Formulas:
# 1^k + 2^k + ... + n^k = a_1 n + a_2 n^2 + ... + a_{k+1} n^(k+1),
# where a_i's are rational coefficients that can be written a
# reduced fractions p_i/q_i (if a_i = 0, we shall consider q_i = 1).
#
# For example, 1^4 + 2^4 + ... + n^4 = -1/30 n + 1/3 n^3 + 1/2 n^4 + 1/5 n^5.
#
# Define D(k) as the value of q_1 for the sum of k'th powers
# (i.e. the denominator of the reduced fraction a1).
# Define F(m) as the m'th value of k ≥ 1 for which D(k) = 20010.
# You are given D(4) = 30 (since a_1 = -1/30),
# D(308) = 20010, F(1) = 308, F(10) = 96404.
#
# Find F(10^5).

# THEORY:
#
# The unit term in the formula for k is the Bernoulli number B(k).
# If k is odd and greater than 1, B(k) is zero, so D(k) is 1.
# If n is even, D(k) is the product of all primes p such that p-1 divides n.
#
# 20010 = 2 * 3 * 5 * 23 * 29.
# Thus if 20010 divides D(k), 1, 2, 4, 22, and 28 divide k;
# that is, 308 = 2^2 * 7 * 11 divides k.
#
# The goal then becomes to scan through multiples of 308 which are
# not divisible by any prime-preceder besides 1, 2, 4, 22, and 28.
# We can use a sieve to accomplish this.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(m = 10 ** 5):
    cap = 3 * 10 ** 6  # by experimentation, this is enough
    primes = primesbelow(cap)
    count = 0
    sieve = [True for x in range(cap)]
    for i in range(1, cap):
        if sieve[i]:
            is_valid = True
            for f in [1, 2, 4, 7, 11, 14, 22, 28, 44, 77, 154, 308]:
                z = f * i + 1
                # Test if z is prime. If it is, we have an issue.
                if z in [2, 3, 5, 23, 29]:
                    # ...unless it's already a divisor of 20010.
                    continue
                z_is_prime = True
                for p in primes:
                    if p ** 2 > z:
                        break
                    if z % p == 0:
                        z_is_prime = False
                        break
                if z_is_prime:
                    is_valid = False
                    break
            if is_valid:
                count += 1
                #print(count, i, 308 * i, sep='\t')
                if count == m:
                    return 308 * i
            else:
                for mult in range(i, cap, i):
                    sieve[mult] = False

if __name__ == "__main__":
    start = time()
    peresult(719, solve(), time() - start)
