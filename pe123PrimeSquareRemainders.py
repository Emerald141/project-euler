##Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the
##remainder when (p_n−1)^n + (p_n+1)^n is divided by p_n^2.
##
##For example, when n = 3, p_3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.
##
##The least value of n for which the remainder first exceeds 10^9 is 7037.
##
##Find the least value of n for which the remainder first exceeds 10^10.

##Similarly to problem 120, the remainder is 2 when n is even, and the
##remainder is 2*p_n*n when n is odd.

from time import time
from peresult import peresult
from primefns import primeabove

def pe123():
        start = time()
        prime = 2
        index = 1
        while prime * index * 2 <= 10 ** 10:
                prime = primeabove(primeabove(prime))
                index += 2
        peresult(123, index, time() - start)

if __name__ == "__main__":
        pe123()
