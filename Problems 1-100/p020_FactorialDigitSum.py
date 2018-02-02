# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2 ** 1000?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from digitfns import digitsum
from probability import factorial

def solve():
    return digitsum(factorial(100))

if __name__ == "__main__":
    start = time()
    peresult(20, solve(), time() - start)
