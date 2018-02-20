# We shall say that an n-digit number is pandigital if it makes use
# of all the digits 1 to n exactly once; for example, the 5-digit
# number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure
# to only include it once in your sum.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import permutations

def solve():
    products = set()
    for perm in permutations(range(1, 10)):
        multiplicand = 1000 * perm[5] + 100 * perm[6] + 10 * perm[7] + perm[8]
        # a * bcde = fghi
        # ab * cde = fghi
        if perm[0] * (1000 * perm[1] + 100 * perm[2] + 10 * perm[3] + perm[4]) \
         == multiplicand or (10 * perm[0] + perm[1]) * \
         (100 * perm[2] + 10 * perm[3] + perm[4]) == multiplicand:
            products.add(multiplicand)
    return sum(products)

if __name__ == "__main__":
    start = time()
    peresult(32, solve(), time() - start)
