# A snowflake of order n is formed by overlaying an equilateral triangle
# (rotated by 180 degrees) onto each equilateral triangle of the same size
# in a snowflake of order n-1. A snowflake of order 1 is a single equilateral
# triangle.
#
# Some areas of the snowflake are overlaid repeatedly.
#
# For an order n snowflake, let A(n) be the number of triangles that are one
# layer thick, and let B(n) be the number of triangles that are three layers
# thick. Define G(n) = gcd(A(n), B(n)).
#
# E.g. A(3) = 30, B(3) = 6, G(3)=6
# A(11) = 3027630, B(11) = 19862070, G(11) = 30
#
# Further, G(500) = 186 and the sum of G(n) from 3 to 500 is 5124.
# Find the sum of G(n) from 3 to 10^7.
#
# THEORY:
#
# Let A0(n) be the number of triangles that are one layer thick in a snowflake
# of order n which border zero regions that are two layers thick.
# Define A1(n), A2(n), and A3(n) similarly.
# Define B0(n), B1(n), B2(n), and B3(n) similarly but with bordering regions
# which are four layers thick.
# Then we get the following transition matrix:
#
# [0 6 0 0 0 0 0 0]
# [0 3 2 0 1 0 0 0]
# [0 1 2 1 2 0 0 0]
# [0 0 0 3 3 0 0 0]
# [0 0 0 0 0 6 0 0]
# [0 0 0 0 0 3 2 0]
# [0 0 0 0 0 1 2 1]
# [0 0 0 0 0 0 0 3]
#
# Call this matrix M. Then
# [A0(n) A1(n) A2(n) A3(n) B0(n) B1(n) B2(n) B3(n)] = [1 0 0 0 0 0 0 0]*M^(n-2).
#
# Note that A(n) = A0(n) + A1(n) + A2(n) + A3(n),
# and B(n) = B0(n) + B1(n) + B2(n) + B3(n).
#
# Through some creative Wolfram'ing, I found these closed form solutions:
# A(n) = 3 * 4^(n-1) - 2 * 3^(n-1)
# B(n) = (4n + 26) * 3^(n-1)) + (9n - 69) * 2^(2n-3)
#
# The GCD of A(n) and B(n) is also the GCD of A(n) and C(n), where
# C(n) = B(n) + (2n+13) * A(n)
#      = (21n + 9) * 2^(2n-3)
# Factor 6 out of both A(n) and C(n) to get:
#     6 * gcd{ 2^(2n-3) - 3^(n-2),
#              (7n + 3) * 2^(2n-3) }
# The first of the terms in the GCD is now odd, so now we have:
#     6 * gcd{ 2^(2n-3) - 3^(n-2),
#              7n + 3}
# This is the most reduction we can do.
# The exponentiation in the first term can be done modulo 7n + 3 without
# affecting the result of the GCD.

# This takes two minutes in Python but it's as optimized as it can be.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import gcd

def solve(cap = 10 ** 7):
    result = 0
    for n in range(3, cap + 1):
        result += 6 * gcd(
            pow(2, 2 * n - 3, 7 * n + 3) - pow(3, n - 2, 7 * n + 3),
            7 * n + 3
        )
    return result

if __name__ == "__main__":
    start = time()
    peresult(570, solve(), time() - start)
