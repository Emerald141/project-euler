##Starting in the top left corner of a 2×2 grid, and
##only being able to move to the right and down, there
##are exactly 6 routes to the bottom right corner.
##
##How many such routes are there through a 20×20 grid?

from time import time
from peresult import peresult
from probability import choose

def pe15():
        start = time()
        result = choose(40, 20)
        peresult(15, result, time() - start)

if __name__ == "__main__":
        pe15()
