##Consider the fraction, n/d, where n and d are positive integers.
##If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
##
##If we list the set of reduced proper fractions for d ≤ 8 in ascending
##order of size, we get:
##
##1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3,
##3/8, 2/5, 3/7,
##1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
##
##It can be seen that there are 3 fractions between 1/3 and 1/2.
##
##How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
##proper fractions for d ≤ 12,000?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
    start = time()
    primeFactors = dict()
    primes = primesbelow(12001)
    result = 0
    for p in primes:
        for mult in range(p, 12001, p):
            if mult in primeFactors:
                primeFactors[mult].append(p)
            else:
                primeFactors[mult] = [p]
    for denom in range(4, 12001):
        lower = denom // 3 + 1
        upper = (denom - 1) // 2
        sieve = [True for x in range(lower, upper + 1)]
        for p in primeFactors[denom]:
            mult = lower + p - (lower % p)
            if lower % p == 0:
                mult -= p
            while mult <= upper:
                sieve[mult - lower] = False
                mult += p
        result += sum(sieve)
    peresult(73, result, time() - start)

if __name__ == "__main__":
    solve()
