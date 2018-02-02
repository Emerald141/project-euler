# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximised?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def solve():
        start = time()
        greatest = 0
        greatestindex = 0
        for p in range(5, 1001):
                solcount = 0
                a = 1
                b = (p ** 2 - 2 * a * p) / (2 * p - 2 * a)
                while a <= b:
                        if a == p:
                                print(p)
                        b = (p ** 2 - 2 * a * p) / (2 * p - 2 * a)
                        if int(b) == b:
                                solcount += 1
                        a += 1
                if solcount > greatest:
                        greatest = solcount
                        greatestindex = p
        peresult(39, greatestindex, time() - start)

if __name__ == "__main__":
        solve()
