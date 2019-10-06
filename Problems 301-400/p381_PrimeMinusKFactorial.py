# For a prime p let S(p) = (∑ (p-k)!) mod(p) for 1 ≤ k ≤ 5.
#
# For example, if p=7,
# (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2!
# = 720 + 120 + 24 + 6 + 2 = 872.
# As 872 mod(7) = 4, S(7) = 4.
#
# It can be verified that ∑ S(p) = 480 for 5 ≤ p < 100.
#
# Find ∑ S(p) for 5 ≤ p < 10^8.

# THEORY:
#
# (p-1)! + (p-2)! = (p-1 + 1) * (p-2)! = p * (p-2)! = 0 mod p
# So we can safely disregard the first two terms.
#
# (p-3)! + (p-4)! + (p-5)! = ((p-3)(p-4) + (p-4) + 1) * (p-5)!
# = 9 * (p-5)! mod p.
#
# The numbers 1, ..., p-1 mod p form a cyclic multiplicative group of order p-1.
# Thus they're generated by some Y.
# Then (p-1)! = Y^0 * Y^1 * Y^2 * ... * Y^(p-2)
#             = Y^(0 + 1 + 2 + ... + (p-2))
#             = Y^( (p-2) * (p-1) / 2 )
#             = (-1)^(p-2)
#             = -1
# because p is odd; therefore (p-1)! = (p-1) mod p, so (p-2)! = 1 mod p.
#
# It follows that S(p) = 9 * (p-2)^-1 * (p-3)^-1 * (p-4)^-1
#                      = 9 * (-24)^-1 mod p
#                      = -3 / 8 mod p.
# If p % 4 = 1, then S(p) = -3 / 8 * (p^2 - 2 * p + 1).
# If p % 4 = 3, then S(p) = -3 / 8 * (3 * p^2 - 4 * p + 1).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 10 ** 8):
    primes = primesbelow(cap)
    result = 0
    for p in primes[2:]:  # Ignoring 2 and 3
        if p % 4 == 1:
            result += -3 * (p ** 2 - 2 * p + 1) // 8 % p
        else:
            result += -3 * (3 * p ** 2 - 4 * p + 1) // 8 % p
    return result

if __name__ == "__main__":
    start = time()
    peresult(381, solve(), time() - start)