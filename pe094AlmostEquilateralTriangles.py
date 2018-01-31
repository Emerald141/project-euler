# It is easily proved that no equilateral triangle exists with integral
# length sides and integral area. However, the almost equilateral triangle
# 5-5-6 has an area of 12 square units.
# 
# We shall define an almost equilateral triangle to be a triangle for which
# two sides are equal and the third differs by no more than one unit.
# 
# Find the sum of the perimeters of all almost equilateral triangles with
# integral side lengths and area and whose perimeters do not exceed one
# billion (1,000,000,000).

# THEORY:
#
# Let the sides of the triangle be a, a, and b.
# By Heron's formula, the area is equal to
# sqrt( (a + b/2) * (b/2) * (b/2) * (a - b/2) ).
# Clearly b must be even, which implies that a is odd.
# 
# If a = 2x + 1 and b = 2x for some x:
# Area = sqrt( (3x + 1) * x * x * (x + 1) )
#      = x * sqrt( 3x^2 + 4x + 1 ).
# This means 3x^2 + 4x + 1 = y^2 for some y.
# Through use of Dario Alpern's diophantine equation solver
# (found at https://www.alpertron.com.ar/QUAD.HTM),
# we can find a recursive formula for (x,y) pairs starting from the trivial
# solutions (x,y) = (0, +/- 1):
#   x_(n+1) = -2 x_n - 1 y_n - 2
#   y_(n+1) = -3 x_n - 2 y_n - 2
# Only pairs where 0 < x <= (cap - 2) / 6 are counted.
#
# If a = 2x - 1 and b = 2x for some x:
# Area = sqrt( (3x - 1) * x * x * (x - 1) )
#      = x * sqrt( 3x^2 - 4x + 1 ).
# This means 3x^2 - 4x + 1 = y^2 for some y.
# For this case, Alpern's program gives these formulas:
#   x_(n+1) = -2 x_n - 1 y_n + 2
#   y_(n+1) = -3 x_n - 2 y_n + 2
# Only pairs where 0 < x <= (cap + 2) / 6 are counted.

from time import time
from peresult import peresult
from math import sqrt

def find_values(seed, seed_sign, recur_sign, limit):
    values = set()
    x = seed
    y = seed_sign * int(sqrt(3 * seed ** 2 + recur_sign * -4 * seed + 1))
    while x <= limit:
        if x > 0:
            values.add(x)
        x, y = -2 * x - y + 2 * recur_sign, -3 * x - 2 * y + 2 * recur_sign
    return values

def pe094(cap = 10 ** 9):
    start = time()
    result = 0
    for recur_sign in [1, -1]:
        values = set()  # To prevent duplication
        for seed_sign in [1, -1]:
            values = values.union(find_values(0, seed_sign, recur_sign, \
                                              (cap + 2) // 6))
        if recur_sign == 1: # a = b + 1
            result += 6 * sum(values) - 2 * len(values)
        else:               # a = b - 1
            result += 6 * sum(values) + 2 * len(values)
    result -= 4  # The 1-1-2 triangle doesn't count.
    peresult(94, result, time() - start)

if __name__ == "__main__":
    pe094()
