##The smallest number m such that 10 divides m! is m=5.
##The smallest number m such that 25 divides m! is m=10.
##
##Let s(n) be the smallest number m such that n divides m!.
##So s(10)=5 and s(25)=10.
##Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
##S(100)=2012.
##
##Find S(10^8).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow
from math import log

primedivs = dict()

def solve(cap):
    start = time()
    primedivs[2] = [0, 2, 4, 4, 6, 8, 8, 8, 10, 12, 12, 14, 16, 16, 16, 16]
    primedivs[3] = [0, 3, 6, 9, 9, 12, 15, 18, 18, 21]
    primedivs[5] = [0, 5, 10, 15, 20, 25, 25]
    result = 0
    sieve = [0 for x in range(cap + 1)]
    for i in range(2, len(sieve)):
        if sieve[i] == 0: #if i is prime
            result += i
            for exponent in range(1, int(log(cap, i)) + 1):
                power = i ** exponent
                for multiple in range(power, cap + 1, power):
                    possibleNew = minFactorial(i, exponent)
                    if possibleNew > sieve[multiple]:
                        sieve[multiple] = possibleNew
        else:
            result += sieve[i]
    peresult(549, result, time() - start)

def minFactorial(base, power):
    if base in primedivs.keys():
        return primedivs[base][power]
    return base * power

if __name__ == "__main__":
    solve(10 ** 8)
