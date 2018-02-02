# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    bignum = 600851475143
    divisor = 2
    while divisor ** 2 < bignum:
        while bignum / divisor % 1 == 0 and bignum > divisor:
            bignum //= divisor
        divisor += 1
    return bignum

if __name__ == "__main__":
    start = time()
    peresult(3, solve(), time() - start)
