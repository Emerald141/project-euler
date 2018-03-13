# A segment is uniquely defined by its two endpoints.
# By considering two line segments in plane geometry there are
# three possibilities:
# the segments have zero points, one point, or infinitely many points in common.
#
# Moreover when two segments have exactly one point in common it might be the
# case that that common point is an endpoint of either one of the segments or
# of both. If a common point of two segments is not an endpoint of either of
# the segments it is an interior point of both segments.
# We will call a common point T of two segments L1 and L2 a true intersection
# point of L1 and L2 if T is the only common point of L1 and L2 and T is an
# interior point of both segments.
#
# Consider the three segments L1, L2, and L3:
#
# L1: (27, 44) to (12, 32)
# L2: (46, 53) to (17, 62)
# L3: (46, 70) to (22, 40)
#
# It can be verified that line segments L2 and L3 have a true intersection
# point. We note that as the one of the end points of L3: (22,40) lies on L1
# this is not considered to be a true point of intersection. L1 and L2 have
# no common point. So among the three line segments, we find one true
# intersection point.
#
# Now let us do the same for 5000 line segments. To this end, we generate
# 20000 numbers using the so-called "Blum Blum Shub" pseudo-random number
# generator.
#
# s(0) = 290797
# s(n+1) = s(n)×s(n) (modulo 50515093)
# t(n) = s(n) (modulo 500)
#
# To create each line segment, we use four consecutive numbers t(n). That is,
# the first line segment is given by:
#
# (t(1), t(2)) to (t(3), t(4))
#
# The first four numbers computed according to the above generator should be:
# 27, 144, 12 and 232. The first segment would thus be (27,144) to (12,232).
#
# How many distinct true intersection points are found among the 5000 line
# segments?

# THEORY:
#
# Note the first line segment as a vector r going from p = (a, b) to (c, d)
# and the second line segment as a vector s going from q = (e, f) to (g, h).
# The two lines intersect if and only if p + tr = q + us for some 0 < t,u < 1.
# Cross each side with s, then solve for t, to get
# t = ((q - p) cross s) / (r cross s).
# Similarly,
# u = ((q - p) cross r) / (r cross s).
# Find the intersection point from this t and u (if they're between 0 and 1)
# and add it to a set that excludes duplicates.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

class Blum_Blum_Shub:
    def __init__(self):
        self.seed = 290797
    def next(self):
        self.seed = self.seed ** 2 % 50515093
        return self.seed % 500

def get_intersection(line1, line2):
    a, b, c, d = line1[0], line1[1], line1[2], line1[3]
    e, f, g, h = line2[0], line2[1], line2[2], line2[3]
    numer1 = (e - a) * (h - f) - (f - b) * (g - e)
    numer2 = (e - a) * (d - b) - (f - b) * (c - a)
    denom = (c - a) * (h - f) - (d - b) * (g - e)
    if denom != 0 and 0 < numer1 / denom < 1 and 0 < numer2 / denom < 1:
        x = ((a * (denom - numer1)) + (c * numer1)) / denom
        y = ((b * (denom - numer1)) + (d * numer1)) / denom
        return (x, y)
    return (0, 0)

def solve(cap = 5000):
    lines = []
    num_gen = Blum_Blum_Shub()  # Random number generator seed
    for line_num in range(cap):
        lines.append((num_gen.next(), num_gen.next(), num_gen.next(),
         num_gen.next()))
    points = set()
    for i in range(1, len(lines)):
        for j in range(i):
            new_point = get_intersection(lines[i], lines[j])
            if new_point[1] != 0:
                points.add(new_point)
    return len(points)

if __name__ == "__main__":
    start = time()
    peresult(165, solve(), time() - start)
