# A small child has a “number caterpillar” consisting of forty jigsaw pieces,
# each with one number on it, which, when connected together in a line,
# reveal the numbers 1 to 40 in order.
#
# Every night, the child's father has to pick up the pieces of the caterpillar
# that have been scattered across the play room. He picks up the pieces at
# random and places them in the correct order.
# As the caterpillar is built up in this way, it forms distinct segments that
# gradually merge together.
# The number of segments starts at zero (no pieces placed), generally increases
# up to about eleven or twelve, then tends to drop again before finishing at a
# single segment (all pieces placed).
#
# For example:
#
# Piece Placed	Segments So Far
# 12	           1
# 4	               2
# 29	           3
# 6	               4
# 34	           5
# 5	               4
# 35	           4
# …	               …

# Let M be the maximum number of segments encountered during a random tidy-up
# of the caterpillar.
# For a caterpillar of ten pieces, the number of possibilities for each M is
#
# M 	Possibilities
# 1	        512
# 2	        250912
# 3	        1815264
# 4	        1418112
# 5	        144000
#
# so the most likely value of M is 3 and the average value is
# 385643/113400 = 3.400732, rounded to six decimal places.
#
# The most likely value of M for a forty-piece caterpillar is 11; but what is
# the average value of M?
#
# Give your answer rounded to six decimal places.

# THEORY:
#
# If you have n ordered segments of the caterpillar, you can:
# * join two segments (effectively removing one): n-1 choices
# * add onto the front or back of a segment: 2n choices
# * make a new segment between two others, or at the front or back: n+1 choices
# Use dynamic programming, keeping track of the max number of segments
# seen thus far.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(size = 40):
    length = (size + 1) // 2
    # grid[c][m] = number of possibilities which currently have c+1 segments
    #              and have had a maximum of m+1 segments over their lifetimes
    grid = [ [0 for m in range(length)] for c in range(length)]
    grid[0][0] = 1  # First piece always makes its own segment
    for piece in range(2, size + 1):
        new_grid = [ [0 for m in range(length)] for c in range(length)]
        for c in range(length):
            for m in range(length):
                # Add to existing segment
                new_grid[c][m] += 2 * (c+1) * grid[c][m]
                # Join two segments
                if c != 0:
                    new_grid[c-1][m] += c * grid[c][m]
                # Create new segment
                if c != length - 1:
                    new_m = max(c+1, m)
                    new_grid[c+1][new_m] += (c+2) * grid[c][m]
        grid = new_grid
    result = sum(grid[0][c] * (c+1) for c in range(length)) / sum(grid[0])
    return round(result, 6)

if __name__ == "__main__":
    start = time()
    peresult(253, solve(), time() - start)
