# Starting in the top left corner of a 2×2 grid, and
# only being able to move to the right and down, there
# are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import choose

def solve(x = 20, y = 20):
    return choose(x + y, x)

if __name__ == "__main__":
    start = time()
    peresult(15, solve(), time() - start)
