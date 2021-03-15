# A number consisting entirely of ones is called a repunit. We shall define
# R(k) to be a repunit of length k.
#
# For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these
# prime factors is 9414.
#
# Find the sum of the first forty prime factors of R(10^9).

# THEORY:
#
# R(k) = (10^k - 1) / 9.
# Therefore, if 10^k mod p = 1, then p divides R(k),
# for any prime p EXCEPT 3 (since 3 divides 9).
# R(k) is divisible by 3 if and only if k is divisible by 3.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(k = 10 ** 9):
    count = 0
    result = 0
    primes = primesbelow(10 ** 6)  # this should be enough
    if k % 3 == 0:
        count = 1
        result = 3
    for p in primes[2:]:
        if pow(10, k, p) == 1:
            count += 1
            result += p
            if count == 40:
                return result
    raise RuntimeError("Prime cap is too low")

if __name__ == "__main__":
    start = time()
    peresult(132, solve(), time() - start)
