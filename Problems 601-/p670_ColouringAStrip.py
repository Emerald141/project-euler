# A certain type of tile comes in three different sizes - 1×1, 1×2, and 1×3 -
# and in four different colours: blue, green, red and yellow. There is an
# unlimited number of tiles available in each combination of size and colour.
#
# These are used to tile a 2×n rectangle, where n is a positive integer,
# subject to the following conditions:
#
# * The rectangle must be fully covered by non-overlapping tiles.
# * It is not permitted for four tiles to have their corners meeting at a
# single point.
# * Adjacent tiles must be of different colours.
#
# For example, the following is an acceptable tiling of a 2×12 rectangle:
#
#     RRGBRRBRYBBB
#     BBGYYGGRYGRR
#
# but the following is not an acceptable tiling, because it violates the
# "no four corners meeting at a point" rule:
#
#     BGGRRRYRYBYY
#     RRYBBGYRGGRR
#
# Let F(n) be the number of ways the 2×n rectangle can be tiled subject to
# these rules. Where reflecting horizontally or vertically would give a
# different tiling, these tilings are to be counted separately.
#
# For example, F(2)=120, F(5)=45876, and F(100)≡53275818 (mod 1000004321).
#
# Find F(10^16) mod 1000004321.

# THEORY:
#
# There are six single-tile components of horizontal tiles:
# a 1x1, the two squares in a 1x2, and the three squares in a 1x3.
# Every vertical 2x1 section of the strip is composed of two of these.
# Thus there are 37 possible vertical sections: 6*6 consisting of components
# of horizontal tiles, and 1 consisting of a single vertical tile.
#
# We can define a transition matrix to determine what sections can follow
# what other sections.
# Multiplying this matrix with itself enough times, and then multiplying an
# initial-state row vector with it, will give our result.

from time import time
from math import log
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matrixmult

def solve(n = 10 ** 16):
    mod = 1000004321
    mat = [ [0 for y in range(37)] for x in range(37)]
    # 0 = 1x2 tile
    # 1 = first of a 1x2
    # 2 = second of a 1x2
    # 3 = first of a 1x3
    # 4 = second of a 1x3
    # 5 = third of a 1x3
    for index1 in range(36):
        top1 = index1 // 6
        bot1 = index1 % 6
        if top1 in [0, 1, 3] and bot1 in [0, 1, 3]:
            mat[36][index1] = 6
        if top1 in [0, 2, 5] and bot1 in [0, 2, 5]:
            mat[index1][36] = 2
            continue
        for index2 in range(36):
            top2 = index2 // 6
            bot2 = index2 % 6
            if (top1 in [1, 3, 4] or top2 in [2, 4, 5]) and top2 != top1 + 1:
                continue
            if (bot1 in [1, 3, 4] or bot2 in [2, 4, 5]) and bot2 != bot1 + 1:
                continue
            entry = [1, 2, 6][(top2 in [0, 1, 3]) + (bot2 in [0, 1, 3])]
            mat[index1][index2] = entry
    mat[36][36] = 3

    # Lifted from problem 458...
    matpows = [mat]
    for twopow in range(int(log(n, 2)) + 1):
        newmat = matrixmult(matpows[-1], matpows[-1])
        for row in range(len(newmat)):
            for col in range(len(newmat[0])):
                newmat[row][col] %= mod
        matpows.append(newmat)
    remaining = n - 1
    rowvector = [[12 * ((x // 6 in [0, 1, 3]) and (x % 6 in [0, 1, 3]))
                    for x in range(36)] + [4]]
    while remaining > 0:
        power = int(log(remaining, 2))
        rowvector = matrixmult(rowvector, matpows[power])
        for index in range(len(rowvector[0])):
            rowvector[0][index] %= mod
        remaining -= 2 ** power
    result = rowvector[0][36]
    for x in range(36):
        if x // 6 in [0, 2, 5] and x % 6 in [0, 2, 5]:
            result += rowvector[0][x]
    return result % mod

if __name__ == "__main__":
    start = time()
    peresult(670, solve(), time() - start)
