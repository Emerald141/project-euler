##In a sliding game a counter may slide horizontally or vertically into
##an empty space. The objective of the game is to move the red counter
##from the top left corner of a grid to the bottom right corner; the
##space always starts in the bottom right corner.
##
##Let S(m,n) represent the minimum number of moves to complete the game
##on an m by n grid. For example, it can be verified that S(5,4) = 25.
##
##There are exactly 5482 grids for which S(m,n) = p^2, where p < 100 is prime.
##
##How many grids does S(m,n) = p^2, where p < 10^6 is prime?

from time import time
from peresult import peresult
from math import sqrt

def pe313(cap):
        start = time()
        sieve = [True for x in range(cap)]
        primesquares = []
        for ind in range(2, int(sqrt(len(sieve))) + 1):
                if sieve[ind]:
                        for multiple in range(ind ** 2, len(sieve), ind):
                                sieve[multiple] = False
                        primesquares.append(ind ** 2)
        for ind in range(int(sqrt(len(sieve))) + 1, len(sieve)):
                if sieve[ind]:
                        primesquares.append(ind ** 2)
        result = 0
        for primesquare in primesquares:
                if primesquare == 4:
                        continue
                #Case for when m > n
                target = (primesquare + 13) // 2
                highm = (target - 2) // 3
                lowm = target // 4 #can't reach this value of m
                while target - 3 * (lowm + 1) >= lowm + 1: #while n >= m
                        lowm += 1
                result += 2 * (highm - lowm)
        peresult(313, result, time() - start)

if __name__ == "__main__":
        pe313(10**6)
