# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    for c in range(335, 998):
        for b in range((1000 - c) // 2 + 1, 999 - c):
            a = 1000 - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

if __name__ == "__main__":
    start = time()
    peresult(9, solve(), time() - start)
