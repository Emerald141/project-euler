# The first two consecutive numbers to have two distinct
# prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct
# prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four
# distinct prime factors. What is the first of these numbers?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 1000000):
    primefactors = [0 for x in range(cap)]
    streak = 0
    for x in range(2, cap):
        if primefactors[x] == 0:
            # x is prime
            streak = 0
            for multiple in range(2 * x, cap, x):
                primefactors[multiple] += 1
        elif primefactors[x] == 4:
            streak += 1
            if streak == 4:
                return x - 3
        else:
            streak = 0
    print("Cap not high enough. Raise and try again.")

if __name__ == "__main__":
    start = time()
    peresult(47, solve(200000), time() - start)
