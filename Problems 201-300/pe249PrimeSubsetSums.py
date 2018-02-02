##Let S = {2, 3, 5, ..., 4999} be the set of prime numbers less than 5000.
##
##Find the number of subsets of S, the sum of whose elements is a prime number.
##Enter the rightmost 16 digits as your answer.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
    start = time()
    print("Note: This one takes a while. Don't know how to get it under 60s.")
    mod = 10 ** 16
    primes = primesbelow(5000)
    totalLargest = 1
    for p in primes:
        totalLargest += p
    subsetCounts = [1] + [0 for x in range(totalLargest)]
    currentLargest = 0
    for p in primes:
        currentLargest += p
        for newSum in range(currentLargest, p-1, -1):
            subsetCounts[newSum] += subsetCounts[newSum - p]
            subsetCounts[newSum] %= mod
    largeprimes = primesbelow(totalLargest)
    result = 0
    for lp in largeprimes:
        result += subsetCounts[lp]
    result %= mod
    peresult(249, result, time() - start)

if __name__ == "__main__":
    solve()
