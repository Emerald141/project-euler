# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 100):
    sum_of_squares = 0
    for x in range(1, cap + 1):
        sum_of_squares += x ** 2
    return (cap * (cap + 1) // 2) ** 2 - sum_of_squares

if __name__ == "__main__":
    start = time()
    peresult(6, solve(), time() - start)
