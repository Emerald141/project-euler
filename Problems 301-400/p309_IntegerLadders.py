# In the classic "Crossing Ladders" problem, we are given the lengths x and y
# of two ladders resting on the opposite walls of a narrow, level street. We
# are also given the height h above the street where the two ladders cross
# and we are asked to find the width of the street (w).
#
# Here, we are only concerned with instances where all four variables are
# positive integers.
# For example, if x = 70, y = 119 and h = 30, we can calculate that w = 56.
#
# In fact, for integer values x, y, h and 0 < x < y < 200, there are only five
# triplets (x,y,h) producing integer solutions for w:
# (70, 119, 30), (74, 182, 21), (87, 105, 35), (100, 116, 35) and
# (119, 175, 40).
#
# For integer values x, y, h and 0 < x < y < 1 000 000, how many triplets
# (x,y,h) produce integer solutions for w?

# THEORY:
#
# It's an equivalent problem to find out how many triplets (x,y,w) produce
# integer solutions for h, and a lot easier problem besides.
#
# Let A = sqrt(x^2 - w^2) and B = sqrt(y^2 - w^2), i.e. the vertical distance
# covered by each ladder.
# Let n be the horizontal distance from the left  wall (where the ladder with
# length x rests) to the point where the ladders cross.
# Then by the principles of similar triangles,
#   w / A = n / h    and    w / B = (w - n) / h.
# Solving the first equation for n, and substituting into the second, yields
#   w / h - w / A = w / B.
# Cross-multiplying gives the formula for h:
#   h = A * B / (A + B).
#
# Assume that A = c * sqrt(d) and B = e * sqrt(f), where c,d,e,f are integers
# and d and f are squarefree. Then:
#   h = c * e * sqrt(df) / (c * sqrt(d) + e * sqrt(f))
#     = c * e * sqrt(df) * (c * sqrt(d) - e * sqrt(f)) / (c^2 * 2 - e^2 * f)
#     = (c^2 * d * e * sqrt(f) - c * e^2 * f * sqrt(d)) / (c^2 * 2 - e^2 * f)
# If h is an integer, then its numerator here must be an integer, since the
# denominator is. It follows that f = d, and therefore
#   h = c * e * d / ((c + e) * sqrt(d))
#     = c * e * sqrt(d) / (c + e)
# which is rational if and only if sqrt(d) is an integer. Since d is assumed
# to be squarefree, d = 1.
# Therefore A and B must both be integers.
#
# Iterate over all right triangles with hypotenuse < 10^6, then record the
# pairs of catheti. For every w below 10^6, check all pairs of paired catheti.
#
# (lifted from problem 075)
# As per F. J. M. Barning, all primitive Pythagorean triples are found in a
# ternary tree rooted at (3,4,5), and the children of each node can be found by
# multiplying each of three matrices by the node's triple.
# The three matrices are:
#     [1 -2 2]      [1, 2, 2]      [-1, 2, 2]
# A = [2 -1 2], B = [2, 1, 2], C = [-2, 1, 2]
#     [2 -2 3]      [2, 2, 3]      [-2, 2, 3]
#
# To find all primitive Pythagorean triples whose sum is at or below the limit,
# simply do a preorder traversal. Stop traversing each branch when the
# hypotenuse of a triple is above the limit.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow
from matrixfns import matrixmult

def solve(cap = 10 ** 6):
    start = time()

    catheti = [ [] for w in range(cap)]

    # Multiplying triples as row vectors on left, so taking matrix transposes
    mat1 = [[1, 2, 2], [-2, -1, -2], [2, 2, 3]]
    mat2 = [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
    mat3 = [[-1, -2, -2], [2, 1, 2], [2, 2, 3]]

    stack = [ [(3, 4, 5), 0] ]  # Last number means how many children in stack

    while len(stack) > 0:
        if stack[-1][1] == 0:   # Node has not been visited
            if stack[-1][0][2] >= cap:  # Hypotenuse is too large
                del stack[-1]
            else:
                for mult in range(stack[-1][0][2], cap, stack[-1][0][2]):
                    cathA = stack[-1][0][0] * (mult // stack[-1][0][2])
                    cathB = stack[-1][0][1] * (mult // stack[-1][0][2])
                    catheti[cathA].append(cathB)
                    catheti[cathB].append(cathA)
                new_triple = tuple(matrixmult((stack[-1][0],), mat1)[0])
                stack[-1][1] = 1
                stack.append([new_triple, 0])
        elif stack[-1][1] == 1:     # First child visited
            new_triple = tuple(matrixmult((stack[-1][0],), mat2)[0])
            stack[-1][1] = 2
            stack.append([new_triple, 0])
        elif stack[-1][1] == 2:     # Second child visited
            new_triple = tuple(matrixmult((stack[-1][0],), mat3)[0])
            stack[-1][1] = 3
            stack.append([new_triple, 0])
        else:                       # All children visited
            del stack[-1]

    result = 0
    for w in range(len(catheti)):
        for i in range(len(catheti[w]) - 1):
            for j in range(i + 1, len(catheti[w])):
                A, B = catheti[w][i], catheti[w][j]
                if (A * B / (A + B)) % 1 == 0:
                    result += 1
    return result

if __name__ == "__main__":
    start = time()
    peresult(309, solve(), time() - start)
