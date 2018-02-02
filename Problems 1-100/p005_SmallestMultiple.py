# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow
from math import log

def solve(cap = 20):
    primes = primesbelow(cap)
    result = 1
    for p in primes:
        result *= p ** int(log(cap, p))
    return result

if __name__ == "__main__":
    start = time()
    peresult(5, solve(), time() - start)
