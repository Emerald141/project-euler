##A permutation is an ordered arrangement of objects. For
##example, 3124 is one possible permutation of the digits
##1, 2, 3 and 4. If all of the permutations are listed
##numerically or alphabetically, we call it lexicographic
##order. The lexicographic permutations of 0, 1 and 2 are:
##
##012   021   102   120   201   210
##
##What is the millionth lexicographic permutation of the
##digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import factorial

def solve():
        start = time()
        digits = [str(x) for x in range(10)]
        permsleft = 1000000
        result = ""
        while len(digits) > 0:
                index = 0
                while factorial(len(digits) - 1) < permsleft:
                        permsleft -= factorial(len(digits) - 1)
                        index += 1
                result += digits[index]
                del digits[index]
        peresult(24, result, time() - start)

if __name__ == "__main__":
        solve()
