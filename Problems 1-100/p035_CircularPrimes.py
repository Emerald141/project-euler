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

def solve():
    result = 4  # 2, 3, 5, and 7
    digits = [1, 3, 7, 9]  # The only terminal digits for poly-digit primes
    for a in digits:
        for b in digits:
            num_2 = 10 * a + b
            if isCircuPrime(num_2, 2):
                result += 1
            for c in digits:
                num_3 = 10 * num_2 + c
                if isCircuPrime(num_3, 3):
                    result += 1
                for d in digits:
                    num_4 = 10 * num_3 + d
                    if isCircuPrime(num_4, 4):
                        result += 1
                    for e in digits:
                        num_5 = 10 * num_4 + e
                        if isCircuPrime(num_5, 5):
                            result += 1
                        for f in digits:
                            num_6 = 10 * num_5 + f
                            if isCircuPrime(num_6, 6):
                                result += 1
    return result

if __name__ == "__main__":
    start = time()
    peresult(35, solve(), time() - start)
