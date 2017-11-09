##It was proposed by Christian Goldbach that every odd composite
##number can be written as the sum of a prime and twice a square.
##
##9 = 7 + 2×1^2
##15 = 7 + 2×2^2
##21 = 3 + 2×3^2
##25 = 7 + 2×3^2
##27 = 19 + 2×2^2
##33 = 31 + 2×1^2
##
##It turns out that the conjecture was false.
##
##What is the smallest odd composite that cannot be written as the
##sum of a prime and twice a square?

from time import time
from peresult import peresult
from primefns import isprime, primesbelow
from math import sqrt

def pe46():
        start = time()
        oddnum = 33
        primes = primesbelow(33)
        while True:
                oddnum += 2
                if isprime(oddnum):
                        primes.append(oddnum)
                        continue
                for prime in primes:
                        if sqrt((oddnum - prime) // 2) % 1 == 0:
                                break
                else:
                        result = oddnum
                        break
        peresult(46, result, time() - start)

if __name__ == "__main__":
        pe46()
