##The binomial coefficient C(10, 3) = 120.
##120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
##So the sum of the terms in the prime factorisation of C(10, 3) is 14. 
##
##Find the sum of the terms in the prime factorisation of C(20000000, 15000000).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(larger, smaller):
    start = time()
    primes = primesbelow(larger)
    result = 0
    for p in primes:
        power = 1
        factorcount = 0
        while p ** power <= larger:
            factorcount += larger // (p ** power)
            factorcount -= (larger - smaller) // (p ** power)
            factorcount -= smaller // (p ** power)
            power += 1
        result += p * factorcount
    peresult(231, result, time() - start)

if __name__ == "__main__":
    solve(20000000, 15000000)
