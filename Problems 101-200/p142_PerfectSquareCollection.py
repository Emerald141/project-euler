# Find the smallest x + y + z with integers x > y > z > 0 such that
# x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.

# THEORY:
#
# We have six equations:
# x + y = a^2
# x - y = b^2
# x + z = c^2
# x - z = d^2
# y + z = e^2
# y - z = f^2
#
# All other variables can be written in terms of a, b, and c:
# e^2 = (x+z) - (x-y) = c^2 - b^2
# f^2 = (x+y) - (x+z) = a^2 - c^2
# d^2 = (x+y) + (x-y) - (x+z) = a^2 + b^2 - c^2
# x + y + z = c^2 + (a^2 - b^2) / 2
#
# Since e^2 is positive, c > b; since f^2 is positive, a > c.
# a and b must either be both even or both odd, because a^2 + b^2 = 2x, which
# is even.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    squares = set([1, 4])
    a = 3
    while True:
        squares.add(a ** 2)
        for c in range(a % 2 + 2, a, 2):
            for b in range(a % 2 + 2, c, 2):
                if c ** 2 - b ** 2 in squares and a ** 2 - c ** 2 in squares \
                 and a ** 2 + b ** 2 - c ** 2 in squares:
                    if c ** 2 - (a ** 2 + b ** 2) // 2 > 0:  # if z > 0
                        return c ** 2 + (a ** 2 - b ** 2) // 2
        a += 1

if __name__ == "__main__":
    start = time()
    peresult(142, solve(), time() - start)
