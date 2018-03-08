# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
# 1219 is the smallest number such that the last digits are formed by p1 whilst
# also being divisible by p2.
#
# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of
# consecutive primes, p2 > p1, there exist values of n for which the last
# digits are formed by p1 and n is divisible by p2. Let S be the smallest of
# these values of n.
#
# Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

# THEORY:
#
# Define:
# 10^k = the smallest power of 10 greater than p2
# d = the inverse of 10^k modulo p2 = (10^k)^(p2-2) mod p2, since p2 is prime
# Then S = ((-p1 * d) mod p2) * 10^k + p1.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow, primeabove

def solve(cap = 1000000):
    primes = primesbelow(cap)
    primes.append(primeabove(primes[-1]))
    ten_power = 1
    result = 0
    for i in range(2, len(primes) - 1):
        if ten_power < primes[i]:
            ten_power *= 10
        d = pow(ten_power, primes[i+1] - 2, primes[i+1])
        result += ((-primes[i] * d) % primes[i+1]) * ten_power + primes[i]
    return result

if __name__ == "__main__":
    start = time()
    peresult(134, solve(), time() - start)
