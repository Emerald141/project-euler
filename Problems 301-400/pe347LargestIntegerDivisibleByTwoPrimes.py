##The largest integer ≤ 100 that is only divisible by both the primes 2 and
##3 is 96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N)
##be the largest positive integer ≤N only divisible by both p and q
##and M(p,q,N)=0 if such a positive integer does not exist.
##
##E.g. M(2,3,100)=96.
##M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
##Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100
##that is divisible by both 2 and 73.
##
##Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.
##
##Find S(10 000 000).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap):
    start = time()
    factors = [[0, 0] for x in range(cap + 1)]
    largests = dict()
    for i in range(2, cap + 1):
        if sum(factors[i]) == 0: #i is prime
            for multiple in range(2 * i, cap + 1, i):
                if factors[multiple][0] == 0:
                    factors[multiple][0] = i
                elif factors[multiple][1] == 0:
                    factors[multiple][1] = i
                else:
                    factors[multiple][1] = -1
        elif factors[i][1] > 0: #i is divisible by two distinct primes
            largests[tuple(factors[i])] = i
    result = 0
    for primepair in largests.keys():
        result += largests[primepair]
    peresult(347, result, time() - start)

if __name__ == "__main__":
    solve(10000000)
