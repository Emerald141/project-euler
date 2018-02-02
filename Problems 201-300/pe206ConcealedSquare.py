##Find the unique positive integer whose square has
##the form 1_2_3_4_5_6_7_8_9_0,
##where each “_” is a single digit.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def solve():
        start = time()
        testnum = int(sqrt(19293949596979899)) - 1
        while True:
                if testnum % 10 != 3 and testnum % 10 != 7:
                        testnum -= 2
                        continue
                square = testnum ** 2
                needs = [square % 10 ** (2*n + 1) // (10 ** (2*n)) for n in range(9)]
                for index in range(len(needs)):
                        if needs[index] != 9 - index:
                                testnum -= 2
                                break
                else:
                        result = testnum * 10
                        break
        peresult(206, result, time() - start)

if __name__ == "__main__":
        solve()
