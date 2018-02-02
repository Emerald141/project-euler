# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from digitfns import digitsum

def solve(base = 2, power = 1000):
    return digitsum(base ** power)

if __name__ == "__main__":
    start = time()
    peresult(16, solve(), time() - start)
