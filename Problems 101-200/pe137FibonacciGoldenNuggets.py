# Consider the infinite polynomial series
# A_F(x) = x*F_1 + x^2*F_2 + x^3*F_3 + ...,
# where F_k is the k'th term in the Fibonacci sequence:
# 1, 1, 2, 3, 5, 8, ... ; that is,
# F_k = F_{k−1} + F_{k−2}, F_1 = 1 and F_2 = 1.
# 
# For this problem we shall be interested in values of x for which
# A_F(x) is a positive integer.
# 
# Surprisingly A_F(1/2) = 2.
# The corresponding values of x for the first five natural numbers
# are shown below.
# 
# x	        A_F(x)
# √2−1	        1
# 1/2	        2
# (√13−2)/3	3
# (√89−5)/8	4
# (√34−3)/5	5
# 
# We shall call A_F(x) a golden nugget if x is rational, because they
# become increasingly rarer; for example, the 10th golden nugget is 74049690.
# 
# Find the 15th golden nugget.

# THEORY:
#
# Let phi = (1 + sqrt(5))/2 and psi = (1 - sqrt(5))/2.
# Then F_n = phi^n/sqrt(5) - psi^n/sqrt(5) (Binet's formula).
# A_F(x) can be broken down into the difference of the two geometric series
# (phi*x)^n/sqrt(5) and (psi*x)^n/sqrt(5), where n is summed from 0 to
# infinity in both cases.
# Then A_F(x) = 1/((1-phi*x)*sqrt(5)) - 1/((1-psi*x)*sqrt(5)).
# Using A as shorthand for A_F(x), this can be algebraically solved for x:
# x = (-A - 1 + sqrt(5A^2 + 2A + 1))/(2A).
# In order for this to be rational, 5A^2 + 2A + 1 = B^2 for some integer B.
#
# Dario Alpem's quadratic Diophantine equation solver
# (found at https://www.alpertron.com.ar/QUAD.HTM)
# yields a recurrence relation that can find (A,B) pairs when given
# an initial list of small seed values:
#   A_{n+1} = -9 A_n + 4 B_n - 2
#   B_{n+1} = 20 A_n - 9 B_n + 4
# The absolute values of the A's continuously increase, so the problem becomes
# finding the first fifteen positive A values for each seed, then finding the
# fifteenth lowest positive A value between them.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def find_nuggets(seed, sign, goal):
    nuggets = set()
    a, b = seed, sign * int(sqrt(5 * seed ** 2 + 2 * seed + 1))
    while len(nuggets) < goal:
        if a > 0:
            nuggets.add(a)
        a, b = -9 * a + 4 * b - 2, 20 * a - 9 * b + 4
    return nuggets

def solve(nugget_index = 15):
    start = time()
    nuggets = set()
    seeds = set()
    for possible_seed in range(10000):
        if sqrt(5 * possible_seed ** 2 + 2 * possible_seed + 1) % 1 == 0:
            seeds.add(possible_seed)
    for seed in seeds:
        if seed not in nuggets:
            nuggets = nuggets.union(find_nuggets(seed, 1, nugget_index))
            nuggets = nuggets.union(find_nuggets(seed, -1, nugget_index))
    result = sorted(nuggets)[nugget_index - 1]
    peresult(137, result, time() - start)

if __name__ == "__main__":
    solve()
