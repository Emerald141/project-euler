##In England the currency is made up of pound, £, and
##pence, p, and there are eight coins in general circulation:
##1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
##
##It is possible to make £2 in the following way:
##
##1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
##
##How many different ways can £2 be made using any number of coins?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    result = 0
    for p200 in range(0, 201, 200):
        for p100 in range(0, 201 - p200, 100):
            for p50 in range(0, 201 - p200 - p100, 50):
                for p20 in range(0, 201 - p200 - p100 - p50, 20):
                    for p10 in range(0, 201 - p200 - p100 - p50 - p20, 10):
                        for p5 in range(0, 201 - p200 - p100 - p50 - p20 - p10, 5):
                            for p2 in range(0, 201 - p200 - p100 - p50 - p20 - p10 - p5, 2):
                                result += 1
    peresult(31, result, time() - start)

if __name__ == "__main__":
    solve()
