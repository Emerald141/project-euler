# In a 3x2 cross-hatched grid, a total of 37 different rectangles could be
# situated within that grid.
# 
# There are 5 grids smaller than 3x2, vertical and horizontal dimensions
# being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is
# cross-hatched, the following number of different rectangles could be
# situated within those smaller grids:
# 
# 1x1: 1 
# 2x1: 4 
# 3x1: 8 
# 1x2: 4 
# 2x2: 18
# 
# Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles
# could be situated within 3x2 and smaller grids.
# 
# How many different rectangles could be situated within 47x43 and smaller
# grids?

# THEORY:
#
# To determine how many diagonally-oriented rectangles of a given size can be
# placed in a cross-hatched grid of a given size, it's necessary to know
# the size of the smallest standard-oriented rectangle that contains one.
# As it turns out, this is different for rectangles whose upper corner is
# in the middle of a grid box, or at the corner of a grid box.
#
# Let r and s be the side lengths of a diagonally-oriented rectangle.
# If the upper corner is at the corner of a grid box, the dimensions of the
# enclosing standard-oriented rectangle are:
#   x = floor((r + 1) / 2) + floor((s + 1) / 2)
#   y = floor((r + s + 1) / 2)
# If the upper corner is in the middle of a grid box:
#   x = 1 + floor(r / 2) + floor(s / 2)
#   y = 1 + floor((r + s) / 2)
# 
# If we have a standard-oriented rectangle with side lengths x and y,
# it can be placed up to (X-x) * (Y-y) times in an X by Y grid.
# Added together, these values represent the sum of a multiplication table
# where one value ranges from 1 to 48-x and the other ranges from 1 to 44-y.
# If we mark this value as C(x,y), it can be recursively defined as:
#   C(48,y) = 0
#   C(x,44) = 0
#   C(x,y) = (48-x)*(44-y) + C(x+1,y) + C(x,y+1) - C(x+1,y+1)

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(horiz_size = 47, vert_size = 43):
    start = time()
    result = 0
    c = [ [0 for y in range(vert_size + 2)] for x in range(horiz_size + 2)]
    for x in range(horiz_size, 0, -1):
        for y in range(vert_size, 0, -1):
            c[x][y] = (horiz_size + 1 - x) * (vert_size + 1 - y) + c[x+1][y] \
                      + c[x][y+1] - c[x+1][y+1]
            result += c[x][y]
    for r in range(1, 2 * min(horiz_size, vert_size)):
        for s in range(1, 2 * min(horiz_size, vert_size) - r + 1):
            # Rectangle with upper corner at corner of grid box
            x = (r + 1) // 2 + (s + 1) // 2
            y = (r + s + 1) // 2
            result += c[x][y]
            
            # Rectangle with upper corner in middle of grid box
            x = 1 + r // 2 + s // 2
            y = 1 + (r + s) // 2
            if x > horiz_size or y > vert_size:
                break
            result += c[x][y]
    peresult(147, result, time() - start)

if __name__ == "__main__":
    solve()
