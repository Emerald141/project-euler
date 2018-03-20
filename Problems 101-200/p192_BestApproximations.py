# Let x be a real number.
# A best approximation to x for the denominator bound d is a rational number
# r/s in reduced form, with s ≤ d, such that any rational number which is
# closer to x than r/s has a denominator larger than d:
#
# |p/q-x| < |r/s-x| ⇒ q > d
#
# For example, the best approximation to √13 for the denominator bound 20 is
# 18/5 and the best approximation to √13 for the denominator bound 30 is
# 101/28.
#
# Find the sum of all denominators of the best approximations to √n for the
# denominator bound 10^12, where n is not a perfect square and 1 < n ≤ 100000.

# THEORY:
#
# All best approximations to a real number are its semiconvergents, where if
# a_n is the nth term in the continued fraction, only semiconvergents a_n / 2
# and above are allowed.
#
# To find the continued fractions for a square root, we assume that
# a = floor((x * √n + y) / z); for initial case a_0, (x, y, z) = (1, 0, 1).
# A bit of analysis yields these recursive equations:
# x' = z * x
# y' = a * z^2 - y * z
# z' = x^2 * n - (y - a * z)^2
# Then a' = floor((x' * √n + y') / z').
# (To prevent memory errors, divide x, y, and z by their gcd.)
#
# Let [a_0; a_1, a_2, a_3, a_4...] be the sequence of continued fractions
# for √n. If h_(-2) = 0, h_(-1) = 1, k_(-2) = 1, and k_(-1) = 0, then
# h_n = a_n * h_(n-1) + h_(n-2) and k_n = a_n * k_(n-1) + k_(n-2).
# If k_n goes over the cap, reduce a_n until either k_n reaches half of its
# original value or k goes under the cap.
# If k_n goes under the cap at exactly half of a_n's original value, check to
# see if it's a better approximation than the previous convergent.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt, gcd

def solve(denom_cap = 10 ** 12, n_cap = 10 ** 5):
    result = 0
    for n in range(n_cap + 1):
        if sqrt(n) % 1 == 0:
            continue # No nontrivial solutions for square n
        h_prev, k_prev = 0, 1
        h, k = 1, 0
        x, y, z = 1, 0, 1
        while k <= denom_cap:
            a = int((x * sqrt(n) + y) / z)
            x, y, z = z * x, a * (z ** 2) - y * z, x ** 2 * n - (y - a * z) ** 2
            h_prev, h = h, a * h + h_prev
            k_prev, k = k, a * k + k_prev
            divisor = gcd(x, gcd(y, z))
            x, y, z = x // divisor, y // divisor, z // divisor
        reduction = (k - denom_cap - 1) // k_prev + 1
        h, k = h - reduction * h_prev, k - reduction * k_prev
        if reduction < a / 2 or (reduction == a / 2 and \
          (4 * n * (k_prev * k) ** 2 > (k_prev * h + h_prev * k) ** 2) \
          == (k_prev * h > h_prev * k)):
          # I.e. h / k is a better approximation than h_prev / k_prev
            result += k
        else:
            result += k_prev
    return result

if __name__ == "__main__":
    start = time()
    peresult(192, solve(), time() - start)
