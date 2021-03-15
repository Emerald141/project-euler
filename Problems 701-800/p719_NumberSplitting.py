# We define an S-number to be a natural number, n, that is a perfect square
# and its square root can be obtained by splitting the decimal representation
# of n into 2 or more numbers then adding the numbers.
#
# For example, 81 is an S-number because sqrt(81) = 8+1.
# 6724 is an S-number: sqrt(6724) = 6+72+4.
# 8281 is an S-number: sqrt(8281) = 8+2+81 = 82+8+1.
# 9801 is an S-number: sqrt(9801) = 98+0+1.
#
# Further we define T(N) to be the sum of all S numbers n <= N.
# You are given T(10^4)=41333.
#
# Find T(10^12)

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import count

def splits(n,r):
    # print(' ', n,r)
    if n == r:
        return True
    if n < r:
        return False
    for pow in count(1):
        term = n % (10 ** pow)
        rest = n // (10 ** pow)
        # print(n, r, rest, term, sep='\t')
        if term > r:
            return False
        if splits(rest, r - term):
            return True

def solve(cap = 10 ** 6):
    result = 0
    for r in range(2, cap + 1):
        if r % 1000 == 0:
            print(r)
        if splits(r ** 2, r):
            result += r ** 2
    return result

if __name__ == "__main__":
    start = time()
    peresult(719, solve(), time() - start)
