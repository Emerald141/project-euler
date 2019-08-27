# A root or zero of a polynomial P(x) is a solution to the equation P(x) = 0.
# Define P_n as the polynomial whose coefficients are the digits of n.
# For example, P_5703(x) = 5x3 + 7x2 + 3.
#
# We can see that:
#
# P_n(0) is the last digit of n,
# P_n(1) is the sum of the digits of n,
# P_n(10) is n itself.
#
# Define Z(k) as the number of positive integers, n, not exceeding k for which
# the polynomial P_n has at least one integer root.
#
# It can be verified that Z(100 000) is 14696.
#
# What is Z(10^16)?

# THEORY:
#
# When x > 0, P_n(x) > 0, so all roots must be negative or 0.
# When x <= -10, the magnitude of the most significant term is greater than the
# sum of the magnitude of all other terms.
# Therefore any integer root must be between -9 and 0, inclusive. So for some
# single-digit nonnegative c, P_n(x) = (x + c) * Q(x) for some polynomial Q
# with (possibly negative) integer coefficients.
#
# The problem can be simplified to iterating over possible combinations of c's,
# and for each combination, counting Q's which result in P's.
#
# The P_n's which have 0 as a root are all those for which n > 0 and
# n % 10 = 0. If the limit is 10^N, there are 10^(N-1) of these.
#
# Given positive root c: for the coefficient a_k of x^k in Q(x), k positive,
# 0 <= a_k * c + a_{k-1} <= 9.
# Also, 1 <= a_0 * c <= 9.
#
# Given two positive roots b and c:
# 0 <= a_k * bc + a_{k-1} * (b + c) + a_{k-2} <= 9.
# Also, 1 <= a_0 * bc <= 9.
# Consequently bc <= 9.
#
# Given three positive roots b, c, and d:
# 0 <= a_k * bcd + a_{k-1} * (bc + bd + cd) + a_{k-2} (b + c + d) + a_{k-3} <= 9.
# Also, 1 <= a_0 * bcd <= 9.
# Consequently bcd <= 9.
#
# Because (x + 1)(x + 2)(x + 3)(x + 4) has unit term 24, and all other
# combinations of distinct positive integer linear terms have greater unit term,
# no P_n(x) has more than three distinct nonzero integer solutions.
# The number of P's can thus be found by three-step inclusion-exclusion,
# and dynamic programming to find the number of results in each step.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import row_matrix_pow_mult
from math import floor, ceil

def solve(N = 16):
    result = 10 ** (N - 1)  # count of n for which P_n(0) = 0
    # Add count of n's with at least one nonzero root
    for c in range(1, 10):
        old_dict = dict()
        for first in range(1, 10):
            if first * c <= 9:
                old_dict[first] = 1
        for size in range(1, N - 1):
            new_dict = dict()
            for entry in old_dict:
                low = ceil(-entry / c)
                high = floor((9 - entry) / c)
                for new_entry in range(low, high + 1):
                    if new_entry in new_dict:
                        new_dict[new_entry] += old_dict[entry]
                    else:
                        new_dict[new_entry] = old_dict[entry]
            old_dict = new_dict
        for entry in old_dict:
            if 0 <= entry <= 9:
                result += old_dict[entry]

    # Subtract count of n's with two nonzero roots
    for b in range(1, 3):
        for c in range(b + 1, 9 // b + 1):
            t1 = b + c
            t2 = b * c
            old_dict = dict()
            for first in range(1, floor(9 / t2) + 1):
                second_low = ceil(-first * t1 / t2)
                second_high = floor((9 - first * t1) / t2)
                for second in range(second_low, second_high + 1):
                    old_dict[(first, second)] = 1
            for size in range(2, N - 2):
                new_dict = dict()
                for entry in old_dict:
                    e0, e1 = entry[0], entry[1]
                    low = ceil((-e0 - e1 * t1) / t2)
                    high = floor((9 - e0 - e1 * t1) / t2)
                    for e2 in range(low, high + 1):
                        if (e1, e2) in new_dict:
                            new_dict[(e1, e2)] += old_dict[entry]
                        else:
                            new_dict[(e1, e2)] = old_dict[entry]
                old_dict = new_dict
            for entry in old_dict:
                e0, e1 = entry[0], entry[1]
                if 0 <= e0 + e1 * (b + c) <= 9 and 0 <= e1 <= 9:
                    result -= old_dict[entry]

    # Add count of n's with three nonzero roots
    # (these two are the only ones with product less than 10)
    for combo in ((1, 2, 3), (1, 2, 4)):
        t1 = combo[0] + combo[1] + combo[2]
        t2 = combo[0] * combo[1] + combo[0] * combo[2] + combo[1] * combo[2]
        t3 = combo[0] * combo[1] * combo[2]
        old_dict = dict()
        for first in range(1, floor(9 / t3) + 1):
            second_low = ceil(-first * t2 / t3)
            second_high = floor((9 - first * t2) / t3)
            for second in range(second_low, second_high + 1):
                third_low = ceil((-first * t1 - second * t2) / t3)
                third_high = floor((9 - first * t1 - second * t2) / t3)
                for third in range(third_low, third_high + 1):
                    old_dict[(first, second, third)] = 1
        for size in range(3, N - 3):
            new_dict = dict()
            for entry in old_dict:
                e0, e1, e2 = entry[0], entry[1], entry[2]
                low = ceil((-e0 - e1 * t1 - e2 * t2) / t3)
                high = floor((9 - e0 - e1 * t1 - e2 * t2) / t3)
                for e3 in range(low, high + 1):
                    if (e1, e2, e3) in new_dict:
                        new_dict[(e1, e2, e3)] += old_dict[entry]
                    else:
                        new_dict[(e1, e2, e3)] = old_dict[entry]
            old_dict = new_dict
        for entry in old_dict:
            e0, e1, e2 = entry[0], entry[1], entry[2]
            if 0 <= e0 + e1 * t1 + e2 * t2 <= 9 and 0 <= e1 + e2 * t1 <= 9  \
             and 0 <= e2 <= 9:
                result += old_dict[entry]

    return result

if __name__ == "__main__":
    start = time()
    peresult(269, solve(), time() - start)
