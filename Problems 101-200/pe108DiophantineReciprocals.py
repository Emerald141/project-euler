##In the following equation x, y, and n are positive integers.
##
##1/x + 1/y = 1/n
##
##For n = 4 there are exactly three distinct solutions:
##
##1/5 + 1/20 = 1/4
##1/6 + 1/12 = 1/4
##1/8 + 1/8 = 1/4
##
##What is the least value of n for which the number of distinct solutions
##exceeds one-thousand?

##THEORY:
##    x and y both have to be greater than n
##    So write x = n + s, y = n + t
##    Simplification yields n^2 = s * t
##    So - what square number has 1999 or more factors?
##    (since this will yield 1000 *pairs* of factors)
##    Take its square root. There's the answer

from primefns import primesbelow
from math import log, ceil
import sys
sys.path.append("../Library")
from peresult import peresult
from time import time

def solve(problemNumber, solutionCount):
    start = time()
    targetSqFacCount = 2 * solutionCount - 1
    primes = primesbelow(100)
    primes = primes[:int(log(targetSqFacCount, 3) + 1)]
    minN = 1
    for prime in primes:
        minN *= prime ** 2
    iterators = [0 for x in range(len(primes))]
    activeIterator = 1
    currentN = 1 #discounting the 2 factors
    currentSqFacCount = 1
    while activeIterator < len(primes):
        if activeIterator == 1:
            #Increase the current prime (which is 3)
            iterators[1] += 2
            currentN *= 9
            currentSqFacCount *= iterators[1] + 1
            currentSqFacCount //= iterators[1] - 1
            #Find the number of 2 factors needed
            iterators[0] = ceil(targetSqFacCount / currentSqFacCount)
            if iterators[0] % 2 == 1:
                iterators[0] -= 1
            if iterators[0] >= iterators[1]:
                #Check for new minimum N
                if minN > currentN and log(minN / currentN, 2) > iterators[0]:
                    minN = currentN * (2 ** iterators[0])
            else:
                activeIterator += 1
        else:
            #Increase the current prime
            iterators[activeIterator] += 2
            currentN *= primes[activeIterator] ** 2
            currentSqFacCount *= iterators[activeIterator] + 1
            currentSqFacCount //= iterators[activeIterator] - 1
            #Change all lesser primes to be equal to this one
            for p in range(activeIterator - 1, 0, -1):
                currentN //= primes[p] ** iterators[p]
                currentN *= primes[p] ** iterators[activeIterator]
                currentSqFacCount //= iterators[p] + 1
                currentSqFacCount *= iterators[activeIterator] + 1
                iterators[p] = iterators[activeIterator]
            #Find the number of 2 factors needed
            iterators[0] = ceil(targetSqFacCount / currentSqFacCount)
            if iterators[0] % 2 == 1:
                iterators[0] -= 1
            if iterators[0] >= iterators[1]:
                #Check for new minimum N
                if log(minN / currentN, 2) > iterators[0]:
                    minN = currentN * (2 ** iterators[0])
                #ONLY DIFFERENT LINE
                activeIterator = 1
            else:
                activeIterator += 1
    peresult(problemNumber, int(minN ** 0.5), time() - start)

if __name__ == "__main__":
    solve(108, 1000)
