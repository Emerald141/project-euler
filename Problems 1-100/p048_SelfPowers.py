# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# 
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        result = 0
        for x in range(1, 1001):
                added = 1
                for y in range(x):
                        added *= x
                        added %= 10 ** 10
                result += added
                result %= 10 ** 10
        peresult(48, result, time() - start)

if __name__ == "__main__":
        solve()
