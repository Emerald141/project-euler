##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?

from time import time
from peresult import peresult

def pe3():
        start = time()
        bignum = 600851475143
        divisor = 2
        while divisor ** 2 < bignum:
                while bignum / divisor % 1 == 0 and bignum > divisor:
                        bignum //= divisor
                divisor += 1
        peresult(3, bignum, time() - start)
        
if __name__ == "__main__":
        pe3()
