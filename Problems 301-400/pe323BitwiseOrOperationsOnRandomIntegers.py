##Let y_0, y_1, y_2,... be a sequence of random unsigned 32 bit integers
##(i.e. 0 ≤ y_i < 2^32, every value equally likely).
##
##For the sequence x_i the following recursion is given:
##
##x_0 = 0 and
##x_i = x_(i-1)| y_(i-1), for i > 0. ( | is the bitwise-OR operator)
##
##It can be seen that eventually there will be an index N such that
##x_i = 2^32 - 1 (a bit-pattern of all ones) for all i ≥ N.
##
##Find the expected value of N. 
##Give your answer rounded to 10 digits after the decimal point.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import choose

def solve():
        start = time()
        oneBits = [0 for x in range(33)]
        oneBits[0] = 1
        totalFinishes = 0
        weightedFinishes = 0
        turn = 1
        oldResult = 0
        newResult = 3
        while oldResult != newResult:
                newOneBits = [0 for x in range(33)]
                for startBits in range(len(oneBits)):
                        for endBits in range(startBits, len(oneBits)):
                                newInstances = choose(32 - startBits, endBits - startBits)
                                newOneBits[endBits] += oneBits[startBits] * newInstances * 2 ** startBits
                totalFinishes *= 2 ** 32
                weightedFinishes *= 2 ** 32
                totalFinishes += newOneBits[-1]
                weightedFinishes += turn * newOneBits[-1]
                newOneBits[-1] = 0
                oneBits = newOneBits
                turn += 1
                oldResult = newResult
                newResult = round(weightedFinishes / totalFinishes, 13)
        result = newResult
        result *= 10 ** 10
        result = round(result, 0)
        result /= 10 ** 10
        peresult(323, result, time() - start)

if __name__ == "__main__":
        solve()
