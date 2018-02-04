# Let (a, b, c) represent the three sides of a right angle triangle with
# integral length sides. It is possible to place four such triangles together
# to form a square with length c.
#
# For example, (3, 4, 5) triangles can be placed together to form a 5 by 5
# square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5
# square can be tiled with twenty-five 1 by 1 squares.
#
#
# However, if (5, 12, 13) triangles were used then the hole would measure
# 7 by 7 and these could not be used to tile the 13 by 13 square.
#
# Given that the perimeter of the right triangle is less than one-hundred
# million, how many Pythagorean triangles would allow such a tiling to
# take place?

# THEORY:
#
# Assume that the Pythagorean triangle is primitive; that is, no integer
# besides 1 divides all three side lengths. Let p be the side length of
# the square hole in the center.
# Then if s is the shortest side of the triangle, and p*k is the hypotenuse,
# s^2 + (s+p)^2 = (pk)^2
# 2s^2 + 2sp + p^2 = p^2 k^2
# This is only possible if p divides s, which means p divides every side
# length of the triangle. Therefore p = 1.
#
# The problem therefore becomes finding all primitive Pythagorean triples
# where the lengths of the catheti differ by 1. (All other tileable squares can
# be produced from this set of triples by scaling each element of a triple up
# by the same factor.)
#
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
# As per F. J. M. Barning, all primitive Pythagorean triples are found in a
# ternary tree rooted at (3,4,5), and the children of each node can be found by
# multiplying each of three matrices by the node's triple.
# The three matrices are:
#     [1 -2 2]      [1, 2, 2]      [-1, 2, 2]
# A = [2 -1 2], B = [2, 1, 2], C = [-2, 1, 2]
#     [2 -2 3]      [2, 2, 3]      [-2, 2, 3]
#
# The second matrix is the only one which preserves the difference between
# the catheti. Both others increase it. Therefore if P = (3,4,5), the triples
# which produce tileable squares are P, B * P, B^2 * P, B^3 * P, ...
#
# The number of tile-producing triples formed from one primitive triple is
# 99,999,999 divided by the sum of the sides, rounded down (i.e. the number of
# integers that the triangle can be scaled up by without going over the side
# length cap).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 10 ** 8):
    result = 0
    a, b, c = 3, 4, 5
    while a + b + c < cap:
        result += (cap - 1) // (a + b + c)
        a, b, c = a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c
    return result

if __name__ == "__main__":
    start = time()
    peresult(139, solve(), time() - start)
