# Consider the infinite polynomial series
# A_G(x) = x*G_1 + x^2*G_2 + x^3*G_3 + ...,
# where F_k is the k'th term of the second order recurrence relation
# G_k = G_{k−1} + G_{k−2}, G_1 = 1 and G_2 = 4;
# that is, 1, 4, 5, 9, 14, 23, ... .
# 
# For this problem we shall be interested in values of x for which
# A_F(x) is a positive integer.
# 
# The corresponding values of x for the first five natural numbers
# are shown below.
# 
# x	        A_G(x)
# (√5−1)/4	1
# 2/5	        2
# (√22−2)/6	3
# (√137−5)/14	4
# 1/2	        5
# 
# We shall call A_G(x) a golden nugget if x is rational, because they
# become increasingly rarer; for example, the 20th golden nugget is 211345365.
# 
# Find the sum of the first thirty golden nuggets.

# THEORY:
#
# This problem is much like problem 137: "Fibonacci golden nuggets".
#
# Let phi = (1 + sqrt(5))/2 and psi = (1 - sqrt(5))/2.
# Solving for the recurrence yields
# G_n = a * phi^n + b * psi^n,
# where a = (-1 + 3 * sqrt(5)) / (2 * sqrt(5))
# and b = (1 + 3 * sqrt(5)) / (2 * sqrt(5)).
# 
# A_G(x) can be broken down into the difference of the two geometric series
# a*(phi*x)^n and b*(psi*x)^n, where n is summed from 1 to infinity in both
# cases.
# Then A_G(x) = a*phi*x/(1-phi*x) - b*psi*x/(1-psi*x).
# Using A as shorthand for A_G(x), this can be reduced to a quadratic in x:
# (A+3)x^2 + (A+1)x - A = 0. 
# In order for x to be rational, 5A^2 + 14A + 1 = B^2 for some integer B.
#
# Dario Alpem's quadratic Diophantine equation solver
# (found at https://www.alpertron.com.ar/QUAD.HTM)
# yields a recurrence relation that can find (A,B) pairs when given
# an initial list of small seed values:
#   A_{n+1} = -9 A_n + 4 B_n - 14
#   B_{n+1} = 20 A_n - 9 B_n + 28
# The absolute values of the A's continuously increase, so the problem becomes
# finding the first thirty positive A values for each seed, then finding the
# sum of the thirty lowest positive A values between them.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def find_nuggets(seed, sign, goal):
    nuggets = set()
    a, b = seed, sign * int(sqrt(5 * seed ** 2 + 14 * seed + 1))
    while len(nuggets) < goal:
        if a > 0:
            nuggets.add(a)
        a, b = -9 * a + 4 * b - 14, 20 * a - 9 * b + 28
    return nuggets

def solve(nugget_index = 30):
    start = time()
    nuggets = set()
    seeds = set()
    for possible_seed in range(10000):
        if sqrt(5 * possible_seed ** 2 + 14 * possible_seed + 1) % 1 == 0:
            seeds.add(possible_seed)
    for seed in seeds:
        if seed not in nuggets:
            nuggets = nuggets.union(find_nuggets(seed, 1, nugget_index))
            nuggets = nuggets.union(find_nuggets(seed, -1, nugget_index))
    result = sum(sorted(nuggets)[:nugget_index])
    peresult(140, result, time() - start)

if __name__ == "__main__":
    solve()
