# It was proposed by Christian Goldbach that every odd composite
# number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the
# sum of a prime and twice a square?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import isprime, primesbelow
from itertools import count
from math import sqrt

def solve():
    primes = primesbelow(33)
    for odd in count(35, 2):
        if isprime(odd):
            primes.append(odd)
            continue
        for prime in primes:
            if sqrt((odd - prime) // 2) % 1 == 0:
                break
        else:
            return odd

if __name__ == "__main__":
    start = time()
    peresult(46, solve(), time() - start)
