# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there are
# many more examples.
#
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.
#
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
#
# Given that L is the length of the wire, for how many values of L <= 1,500,000
# can exactly one integer sided right angle triangle be formed?

# THEORY:
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
# To find all primitive Pythagorean triples whose sum is at or below the limit,
# simply do a preorder traversal. Stop traversing each branch when the sum of
# a triple is above the limit.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matrixmult

def solve(cap = 1500000):
    start = time()

    # Multiplying triples as row vectors on left, so taking matrix transposes
    mat1 = [[1, 2, 2], [-2, -1, -2], [2, 2, 3]]
    mat2 = [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
    mat3 = [[-1, -2, -2], [2, 1, 2], [2, 2, 3]]

    # False means no triple sums to the index.
    # True means one triple does.
    # None means at least two do.
    triple_sums = [False for x in range(cap + 1)]

    stack = [ [(3, 4, 5), 0] ]  # Last number means how many children in stack

    while len(stack) > 0:
        if stack[-1][1] == 0:   # Node has not been visited
            this_sum = sum(stack[-1][0])
            if this_sum > cap:  # Triple is too large
                del stack[-1]
            else:
                for multiple in range(this_sum, cap + 1, this_sum):
                    if triple_sums[multiple] == False:
                        triple_sums[multiple] = True
                    elif triple_sums[multiple]:
                        triple_sums[multiple] = None
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
    for triple_sum in triple_sums:
        if triple_sum:
            result += 1
    peresult(75, result, time() - start)

if __name__ == "__main__":
    solve()
