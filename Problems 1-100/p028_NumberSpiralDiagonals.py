# Starting with the number 1 and moving to the right in a
# clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the
# diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a
# 1001 by 1001 spiral formed in the same way?

# THEORY:
#
# The numbers to be summed are:
# 1
# 1+2*1, 1+2*2, 1+2*3, 1+2*4
# 1+2*4+4*1, 1+2*4+4*2, 1+2*4+4*3, 1+2*4+4*4
# 1+2*4+4*4+6*1, 1+2*4+4*4+6*2, 1+2*4+4*4+6*3, 1+2*4+4*4+6*4
# etc.
#
# This can be calculated out to:
# 1*2001 + 2*7994 + 4*7978 + 6*7962 + ... +
# = 2001 + sum of (10 + 16i)(1000 - 2i) for i from 0 to 500
# Or, more generally:
# 2n - 1 + sum of (10 + 16i)(n - 1 - 2i) for i from 0 to (n-1)/2
# where n is one dimension of the spiral.
#
# Wolfram|Alpha solves the above formula explicitly as
# (4n^3 + 3n^2 + 8n - 9) / 6.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(side = 1001):
    return (4 * side ** 3 + 3 * side ** 2 + 8 * side - 9) // 6

if __name__ == "__main__":
    start = time()
    peresult(28, solve(), time() - start)
