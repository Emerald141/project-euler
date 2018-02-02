# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import factorial

def solve():
        start = time()
        fact = [factorial(x) for x in range(10)]
        limit = 6 * fact[9]
        result = 0
        for x in range(10, limit):
                num = x
                factdigsum = 0
                while num > 0:
                        factdigsum += fact[num % 10]
                        num //= 10
                if factdigsum == x:
                        result += x
        peresult(34, result, time() - start)

if __name__ == "__main__":
        solve()
