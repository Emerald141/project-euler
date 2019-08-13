# Given is the arithmetic-geometric sequence u(k) = (900-3k)r^(k-1).
# Let s(n) = Σk=1...n u(k).
#
# Find the value of r for which s(5000) = -600,000,000,000.
#
# Give your answer rounded to 12 places behind the decimal point.

# THEORY:
# This one's pretty straightforward, actually. Just a binary search.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def value(r):
    result = 0
    mult_term = 1
    add_term = 897
    for k in range(1, 5001):
        result += mult_term * add_term
        mult_term *= r
        add_term -= 3
    return result

def solve(target = -6 * 10 ** 11):
    left, right = 1, 2
    while right - left > 10 ** -13:
        mid = (left + right) / 2
        new_val = value(mid)
        if new_val < target:
            right = mid
        else:
            left = mid
    return '{0:.{1}f}'.format(left, 12)

if __name__ == "__main__":
    start = time()
    peresult(235, solve(), time() - start)
