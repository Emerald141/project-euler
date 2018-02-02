# There are exactly fourteen triangles containing a right angle that
# can be formed when each co-ordinate lies between 0 and 2 inclusive;
# that is, 0 ≤ x1, y1, x2, y2 ≤ 2.
# 
# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from fractions import Fraction

def solve(limit):
    start = time()
    result = 3 * (limit ** 2) #Tri's with one or both edges on a major axis
    #(x1, y1) is the point opposite the hypoteneuse
    for x1 in range(1, limit + 1):
        for y1 in range(1, limit + 1):
            slope = Fraction(-x1, y1)
            x2, y2 = x1, y1
            #Counterclockwise
            while x2 >= 0 and y2 <= limit:
                x2 -= slope.denominator
                y2 -= slope.numerator
                if x2 >= 0 and y2 <= limit:
                    result += 1
            x2, y2 = x1, y1
            #Clockwise
            while x2 <= limit and y2 >= 0:
                x2 += slope.denominator
                y2 += slope.numerator
                if x2 <= limit and y2 >= 0:
                    result += 1
    peresult(91, result, time() - start)

if __name__ == "__main__":
    solve(50)
