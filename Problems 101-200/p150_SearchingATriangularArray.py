# In a triangular array of positive and negative integers, we wish to find
# a sub-triangle such that the sum of the numbers it contains is the smallest
# possible.
#
# We wish to make such a triangular array with one thousand rows, so we
# generate 500500 pseudo-random numbers sk in the range ±219, using a type o
# random number generator (known as a Linear Congruential Generator) as follows:
#
# t := 0
# for k = 1 up to k = 500500:
#     t := (615949*t + 797807) modulo 2^20
#     s_k := t−2^19
#
# Thus: s_1 = 273519, s_2 = −153582, s_3 = 450905 etc
#
# Our triangular array is then formed using the pseudo-random numbers thus:
#
#          s_1
#       s_2   s_3
#    s_4   s_5   s_6
# s_7   s_8   s_9   s_10
#          ...
#
# Sub-triangles can start at any element of the array and extend down as far
# as we like (taking-in the two elements directly below it from the next row,
# the three elements directly below from the row after that, and so on).
# The "sum of a sub-triangle" is defined as the sum of all the elements it
# contains.
# Find the smallest possible sub-triangle sum.

# THEORY:
#
# Instead of storing the triangular array directly, store each element as the
# sum of the elements in that row of the triangular array up to that point.
# E.g. if a row is [4, -6, 33, -90], store it as [4, -2, 31, -59].
# Other than that, no special tricks; just brute-force.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(row_count = 1000):
    # Create and fill the modified triangular array
    array = [ [0 for col in range(row + 1)] for row in range(row_count)]
    t = 0
    row, col = 0, 0
    for row in range(len(array)):
        t = (615949 * t + 797807) % (2 ** 20)
        array[row][0] = t - (2 ** 19)
        for col in range(1, row + 1):
            t = (615949 * t + 797807) % (2 ** 20)
            array[row][col] = array[row][col - 1] + t - (2 ** 19)
    # Scan the array for the minimum sum
    min_sum = array[0][0]
    for start_row in range(len(array)):
        for start_col in range(start_row + 1):
            current_sum = 0
            for depth in range(len(array) - start_row):
                current_sum += array[start_row + depth][start_col + depth]
                if start_col > 0:
                    current_sum -= array[start_row + depth][start_col - 1]
                min_sum = min(min_sum, current_sum)
    return min_sum

if __name__ == "__main__":
    start = time()
    peresult(150, solve(), time() - start)
