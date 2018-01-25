# Let H(n) be the number of distinct integer sided equiangular
# convex hexagons with perimeter not exceeding n.
# Hexagons are distinct if and only if they are not congruent.
#
# You are given H(6) = 1, H(12) = 10, H(100) = 31248.
# Find H(55106).

# THEORY:
#
# The sides of an equiangular hexagon can be separated into three
# parallel pairs: a <= a', b <= b', c <= c', and a <= b <= c.
# Furthermore, a' - a = b' - b = c' - c,
# and a, b, and c are not adjacent to each other
# (or else the sides wouldn't form a closed polygon.)
# The side order, clockwise, thus goes a -> b' -> c -> a' -> b -> c'
# or a -> c' -> b -> a' -> c -> b'.
# These two hexagons are congruent.
#
# The problem therefore simplifies to finding all 4-tuples (a, b, c, d)
# where 1 <= a <= b <= c, 0 <= d, and 2(a + b + c) + 3 * d <= n.
#
# Let F(n) be the number of such tuples for which 2(a + b + c) + 3 * d = n.
# If n <= 5, F(n) = 0.
#
# Consider any 4-tuple (a, b, c, d) which is counted in F(n).
# If a > 1, then a tuple (a-1, b-1, c-1, d) is counted in F(n-6).
# Similarly, any such tuple counted in F(n-6) corresponds to a tuple in F(n).
# Therefore F(n) = F(n-6) + F'(n),
# where F'(n) is the number of tuples with a = 1.
#
# If a = 1 and we fix d, then 2 * b + 2 * c = n - 3d - 2.
# (Note that d must have the same divisibility by 2 as n does.)
# b can vary between 1 and floor((n - 3d - 2) / 4), so there are
# floor((n - 3d - 2) / 4) tuples included in F(n) for that value of d.
# Thus F'(n) = floor((n - 2) / 4) + floor((n - 5) / 4) + floor((n - 8) / 4)...
#
# Some mathematical analysis reveals the following formula:
# F'(n) = (x' * x) - (3 * x * (x + 1) / 2) + (y' * y) - (3 * y * (y + 1) / 2)
# where x, x', y, and y' are dependent on n modulo 4.
#
# n = 4 * w:     x = floor((w + 2) / 3), y = floor((w + 1) / 3)
# n = 4 * w + 1: x = floor((w + 2) / 3), y = floor(w / 3)
# n = 4 * w + 2: x = floor((w + 3) / 3), y = floor((w + 1) / 3)
# n = 4 * w + 3: x = floor((w + 2) / 3), y = floor((w + 1) / 3)
#
# In all cases, x' and y' are the numerators of the fractions in the floor
# functions that define x and y, respectively (e.g. if n = 4 * w, x' = w + 2).
#
# Find H(n) by summing F(i) where i <= n.

from time import time
from peresult import peresult
from math import floor

def pe600(cap = 55106):
    start = time()
    hexagon_counts = [0 for i in range(6)]  # Stores most recent 6 F(i) values
    result = 0
    for perimeter in range(6, cap + 1):
        hexagon_counts = hexagon_counts[1:] + [hexagon_counts[0]]
        w = perimeter // 4
        if perimeter % 4 == 0 or perimeter % 4 == 3:
            x = (w + 2) // 3
            xP = w + 2
            y = (w + 1) // 3
            yP = w + 1
        elif perimeter % 4 == 1:
            x = (w + 2) // 3
            xP = w + 2
            y = w // 3
            yP = w
        else:
            x = (w + 3) // 3
            xP = w + 3
            y = (w + 1) // 3
            yP = w + 1
        hexagon_counts[5] += (xP * x) - (3 * x * (x + 1) // 2) \
                                + (yP * y) - (3 * y * (y + 1) // 2)
        result += hexagon_counts[5]
    peresult(600, result, time() - start)

if __name__ == "__main__":
    pe600(55106)
