# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import isprime
from math import sqrt

def solve():
        start = time()
        sieve = [False, False] + [True for x in range(2, 10 ** 6 // 2)]
        primesum = 0
        primes = []
        for index in range(int(sqrt(len(sieve))) + 1):
                if sieve[index]:
                        primesum += index
                        if primesum > 10 ** 6:
                                primesum -= index
                                break
                        primes.append(index)
                        for multiple in range(2 * index, len(sieve), index):
                                sieve[multiple] = False
        finished = False
        print(len(primes))
        print(primes[-1])
        for snippedcount in range(len(primes) - 1):
                for startsnipped in range(snippedcount + 1):
                        beginsnip = sum(primes[:startsnipped])
                        endsnip = sum(primes[len(primes) - snippedcount + startsnipped:])
                        testprime = primesum - beginsnip - endsnip
                        if testprime > 10 ** 6:
                                continue
                        if isprime(testprime):
                                result = testprime
                                finished = True
                if finished:
                        break
        peresult(50, result, time() - start)

if __name__ == "__main__":
        solve()
                        
