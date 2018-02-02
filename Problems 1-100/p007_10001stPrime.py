# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
    primes = primesbelow(200000)
    return primes[10000]

if __name__ == "__main__":
    start = time()
    peresult(7, solve(), time() - start)
