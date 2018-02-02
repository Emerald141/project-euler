# The number, 197, is called a circular prime because all
# rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17,
# 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import isprime
from numassemble import numassemble

def solve():
        start = time()
        result = 4 #2, 3, 5, and 7
        digits = [1, 3, 7, 9]
        for a in digits:
                for b in digits:
                        twonum = numassemble(a, b)
                        if isCircuPrime(twonum, 2):
                                result += 1
                        for c in digits:
                                threenum = numassemble(a, b, c)
                                if isCircuPrime(threenum, 3):
                                        result += 1
                                for d in digits:
                                        fournum = numassemble(a, b, c, d)
                                        if isCircuPrime(fournum, 4):
                                                result += 1
                                        for e in digits:
                                                fivenum = numassemble(a, b, c, d, e)
                                                if isCircuPrime(fivenum, 5):
                                                        result += 1
                                                for f in digits:
                                                        sixnum = numassemble(a, b, c, d, e, f)
                                                        if isCircuPrime(sixnum, 6):
                                                                result += 1
        peresult(35, result, time() - start)

def isCircuPrime(num, digitcount):
        if not isprime(num):
                return False
        for iteration in range(digitcount - 1):
                num *= 10
                num += num // (10 ** digitcount)
                num %= 10 ** digitcount
                if not isprime(num):
                        return False
        return True

if __name__ == "__main__":
        solve()
