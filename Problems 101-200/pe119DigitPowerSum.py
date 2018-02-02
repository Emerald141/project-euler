##The number 512 is interesting because it is equal to the
##sum of its digits raised to some power: 5 + 1 + 2 = 8,
##and 8 ** 3 = 512. Another example of a number with this
##property is 614656 = 28 ** 4.
##
##We shall define an to be the nth term of this sequence
##and insist that a number must contain at least two digits
##to have a sum.
##
##You are given that a2 = 512 and a10 = 614656.
##
##Find a30.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from digitfns import digitsum

def solve():
        start = time()
        pownums = []
        for base in range(2, 100):
                for exp in range(2, 100):
                        if digitsum(base ** exp) == base:
                                pownums.append(base ** exp)
        pownums.sort()
        pownums = pownums[:30]
        peresult(119, pownums[-1], time() - start)

if __name__ == "__main__":
        solve()
