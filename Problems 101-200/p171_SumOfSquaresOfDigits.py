# For a positive integer n, let f(n) be the sum of the squares of the
# digits (in base 10) of n, e.g.
#
# f(3) = 3^2 = 9,
# f(25) = 2^2 + 5^2 = 4 + 25 = 29,
# f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36
#
# Find the last nine digits of the sum of all n, 0 < n < 10^20, such that
# f(n) is a perfect square.

# THEORY:
#
# Let g(k, d) be the sum of all d-digit numbers whose digits squared sum to k,
# and let h(k, d) be the count of all such numbers.
# Then g(k, d+1) = 10 * g(k-0, d) + 0 * h(k-0, d)
#                + 10 * g(k-1, d) + 1 * h(k-1, d)
#                + 10 * g(k-4, d) + 2 * h(k-4, d)
#                + 10 * g(k-9, d) + 3 * h(k-9, d)
#                + ...
#                + 10 * g(k-81, d) + 9 * h(k-81, d)
# and h(k, d+1) = h(k-0, d) + h(k-1, d) + h(k-4, d) + ... + h(k-81, d).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(digit_cap = 20, mod = 10 ** 9):
    sums = [0 for k in range(81 * digit_cap + 1)]
    counts = [0 for k in range(81 * digit_cap + 1)]
    for first_digit in range(1, 10):  # No leading 0's
        sums[first_digit ** 2] = first_digit
        counts[first_digit ** 2] = 1
    result = 45  # Sum of 1 to 9
    for digit_count in range(2, digit_cap + 1):
        for k in range(81 * digit_count, -1, -1):
            sums[k] *= 10
            for minus_base in range(1, 10):
                if k - minus_base ** 2 >= 0:
                    sums[k] += 10 * sums[k - minus_base ** 2] \
                            + minus_base * counts[k - minus_base ** 2]
                    counts[k] += counts[k - minus_base ** 2]
            sums[k] %= mod
            counts[k] %= mod
        for square_base in range(int(len(sums) ** .5) + 1):
            result += sums[square_base ** 2]
            result %= mod
    return result

if __name__ == "__main__":
    start = time()
    peresult(171, solve(), time() - start)
