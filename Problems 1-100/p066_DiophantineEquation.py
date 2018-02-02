# Consider quadratic Diophantine equations of the form:
# 
# x^2 – D * y^2 = 1
# 
# For example, when D=13, the minimal solution in x is
# 649^2 – 13 * 180^2 = 1.
# 
# It can be assumed that there are no solutions in positive integers
# when D is square.
# 
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
# the following:
# 
# 3^2 – 2*2^2 = 1
# 2^2 – 3*1^2 = 1
# 9^2 – 5*4^2 = 1
# 5^2 – 6*2^2 = 1
# 8^2 – 7*3^2 = 1
# 
# Hence, by considering minimal solutions in x for D ≤ 7, the largest
# x is obtained when D=5.
# 
# Find the value of D ≤ 1000 in minimal solutions of x for which the
# largest value of x is obtained.

# THEORY:
#
# The quadratic Diophantine equation given by the problem is also known
# as Pell's equation, after John Pell. (Pell actually had nothing to do
# with this equation; the name is due to a mistake by Euler.)
#
# Existing theory holds that for some convergent h/k to √D,
# (x, y) = (h, k) is a solution to Pell's equation for given D.
# The problem thus becomes finding convergents to √D until one of them
# is a solution.
#
# To find the continued fractions for a square root, we assume that
# a = floor((x * √D + y) / z); for initial case a_0, (x, y, z) = (1, 0, 1).
# A bit of analysis yields these recursive equations:
# x' = z * x
# y' = a * z^2 - y * z
# z' = x^2 * D - (y - a * z)^2
# Then a' = floor((x' * √D + y') / z').
# (To prevent memory errors, divide x, y, and z by their gcd.)
#
# Let [a_0; a_1, a_2, a_3, a_4...] be the sequence of continued fractions
# for √D. If h_(-2) = 0, h_(-1) = 1, k_(-2) = 1, and k_(-1) = 0, then
# h_n = a_n * h_(n-1) + h_(n-2) and k_n = a_n * k_(n-1) + k_(n-2).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt, gcd

def solve(cap = 1000):
    start = time()
    result = -1
    largest = -1
    for D in range(1, cap + 1):
        if sqrt(D) % 1 == 0:
            continue # No nontrivial solutions for square D
        h_prev, k_prev = 0, 1
        h, k = 1, 0
        x, y, z = 1, 0, 1
        while h ** 2 - D * k ** 2 != 1 or k == 0:
            a = int((x * sqrt(D) + y) / z)
            x, y, z = z * x, a * (z ** 2) - y * z, x ** 2 * D - (y - a * z) ** 2
            h_prev, h = h, a * h + h_prev
            k_prev, k = k, a * k + k_prev
            divisor = gcd(x, gcd(y, z))
            x, y, z = x // divisor, y // divisor, z // divisor
        if h > largest:
            largest = h
            result = D
    peresult(66, result, time() - start)

if __name__ == "__main__":
    solve()
