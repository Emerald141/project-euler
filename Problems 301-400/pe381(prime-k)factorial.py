##For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.
##
##For example, if p=7,
##(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)!
##= 6! + 5! + 4! + 3! + 2!
##= 720+120+24+6+2
##= 872.
##As 872 mod(7) = 4, S(7) = 4.
##
##It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.
##
##Find ∑S(p) for 5 ≤ p < 10^8.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap):
    start = time()
    primes = primesbelow(cap)
    print("Finished finding primes")
    factorial = 1 #Factorial of p-5
    result = 4 #p=5 is a special case so I'm ignoring it
    nextIndex = 3 #Index of the next prime to be examined
    counter = 6
    while nextIndex < len(primes):
        factorial *= counter - 5
        if counter == primes[nextIndex]:
            result += (9 * factorial) % primes[nextIndex]
            nextIndex += 1
        counter += 1
    peresult(381, result, time() - start)

if __name__ == "__main__":
    solve(10 ** 8)
