# It is well known that if the square root of a natural number is
# not an integer, then it is irrational. The decimal expansion of
# such square roots is infinite without any repeating pattern at all.
# 
# The square root of two is 1.41421356237309504880..., and the digital
# sum of the first one hundred decimal digits is 475.
# 
# For the first one hundred natural numbers, find the total of the
# digital sums of the first one hundred decimal digits for all the
# irrational square roots.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def solve():
        start = time()
        result = 0
        for num in range(1, 101):
                if sqrt(num) % 1 == 0:
                        continue
                bignum = num * (10 ** 198)
                squareroot = 0
                for tenpower in range(99, -1, -1):
                        test = 0
                        while (squareroot + 10 ** tenpower) ** 2 < bignum:
                                squareroot += 10 ** tenpower
                                result += 1
                                test += 1
        peresult(80, result, time() - start)

if __name__ == "__main__":
        solve()
