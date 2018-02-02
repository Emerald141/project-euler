##A set of disks numbered 1 through 100 are placed
##in a line in random order.
##
##What is the probability that we have a partial
##derangement such that exactly 22 prime number discs
##are found away from their natural positions?
##(Any number of non-prime disks may also be found in
## or out of their natural positions.)
##
##Give your answer rounded to 12 places behind the
##decimal point in the form 0.abcdefghijkl.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import factorial, choose

def solve():
        start = time()
        live, dead = 21, 75
        for turn in range(20, -1, -1):
                live, dead = (live + dead) * turn, 76 * live + 75 * dead
        result = dead * factorial(75) * choose(25, 3) / factorial(100)
        result *= 10 ** 13
        result = round(int(result), -1)
        result /= 10 ** 13
        peresult(239, result, time() - start)

if __name__ == "__main__":
        solve()
