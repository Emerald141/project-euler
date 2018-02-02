##For an integer n ≥ 4, we define the lower prime square root of n, denoted by
##lps(n), as the largest prime ≤ √n and the upper prime square root of n,
##ups(n), as the smallest prime ≥ √n.
##
##So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
##Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n)
##divides n, but not both.
##
##The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are
##8, 10 and 12.
##15 is not semidivisible because it is a multiple of both lps(15) = 3 and
##ups(15) = 5.
##As a further example, the sum of the 92 semidivisible numbers up to 1000 is
##34825.
##
##What is the sum of all semidivisible numbers not exceeding 999966663333 ?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow, primeabove

def solve(limit):
        start = time()
        primes = primesbelow(int(limit ** .5) + 1)
        result = 0
        for ind in range(len(primes) - 1):
                lowPrime = primes[ind]
                highPrime = primes[ind + 1]
                lowSquare = lowPrime ** 2
                highSquare = highPrime ** 2
                #Adding multiples of lowPrime
                bottomMult = lowSquare + lowPrime
                multCount = (highSquare - bottomMult) // lowPrime + 1
                topMult = lowSquare + (multCount * lowPrime)
                result += multCount * (topMult + bottomMult) // 2
                #Adding multiples of highPrime
                topMult = highSquare - highPrime
                multCount = (topMult - lowSquare) // highPrime + 1
                bottomMult = highSquare - (multCount * highPrime)
                result += multCount * (topMult + bottomMult) // 2
                #Subtracting multiple of both
                result -= 2 * lowPrime * highPrime
        #Case of final prime
        lowPrime = primes[-1]
        highPrime = primeabove(lowPrime)
        lowSquare = lowPrime ** 2
        #Adding multiples of lowPrime
        bottomMult = lowSquare + lowPrime
        multCount = (limit - bottomMult) // lowPrime + 1
        topMult = lowSquare + (multCount * lowPrime)
        result += multCount * (topMult + bottomMult) // 2
        #Adding multiples of highPrime
        topMult = limit // highPrime * highPrime
        multCount = (topMult - lowSquare) // highPrime + 1
        bottomMult = topMult - ((multCount - 1) * highPrime)
        result += multCount * (topMult + bottomMult) // 2
        #Possibly subtracting multiple of both
        if lowPrime * highPrime <= limit:
                result -= 2 * lowPrime * highPrime
        #Result
        peresult(234, result, time() - start)

if __name__ == "__main__":
        solve(999966663333)
                
