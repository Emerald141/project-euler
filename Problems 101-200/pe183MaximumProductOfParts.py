##Let N be a positive integer and let N be split into k equal parts,
##r = N/k, so that N = r + r + ... + r.
##Let P be the product of these parts, P = r × r × ... × r = r ** k.
##
##For example, if 11 is split into five equal parts,
##11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.
##
##Let M(N) = P_max for a given value of N.
##
##It turns out that the maximum for N = 11 is found by splitting eleven
##into four equal parts which leads to P_max = (11/4) ** 4; that is,
##M(11) = 14641/256 = 57.19140625, which is a terminating decimal.
##
##However, for N = 8 the maximum is achieved by splitting it into three
##equal parts, so M(8) = 512/27, which is a non-terminating decimal.
##
##Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if
##M(N) is a terminating decimal.
##
##For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.
##
##Find ΣD(N) for 5 ≤ N ≤ 10000.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import e
from fractions import Fraction

def solve(lowest, highest):
        start = time()
        result = 0
        for n in range(lowest, highest + 1):
                k = round(n / e)
                denom = Fraction(n, k).denominator
                while denom % 2 == 0:
                        denom //= 2
                while denom % 5 == 0:
                        denom //= 5
                if denom == 1:
                        result -= n
                else:
                        result += n
        peresult(183, result, time() - start)

if __name__ == "__main__":
        solve(5, 10000)
