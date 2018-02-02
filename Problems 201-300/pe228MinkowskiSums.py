# Let S_n be the regular n-sided polygon – or shape – whose vertices
# v_k (k = 1,2,…,n) have coordinates:
# 
# x_k   =   cos( (2k-1)/n * 180° )
# y_k   =   sin( (2k-1)/n * 180° )
# 
# Each S_n is to be interpreted as a filled shape consisting of all
# points on the perimeter and in the interior.
# 
# The Minkowski sum, S+T, of two shapes S and T is the result of
# adding every point in S to every point in T, where point addition
# is performed coordinate-wise: (u, v) + (x, y) = (u+x, v+y).
# 
# How many sides does S_1864 + S_1865 + … + S_1909 have?

# THEORY:
#
# Each side of the Minkowski sum of S and T is oriented the same way
# as a side in S or in T. This means that if S and T have two sides
# that are oriented the same way (e.g. two vertical sides on the right),
# those sides are only counted once in total.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(low = 1864, high = 1909):
    start = time()
    sides = set()
    for denominator in range(low, high + 1):
        for numerator in range(denominator):
            sides.add(numerator / denominator)
    result = len(sides)
    peresult(228, result, time() - start)

if __name__ == "__main__":
    solve()
