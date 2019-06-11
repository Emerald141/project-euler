# A positive integer with k (decimal) digits is called balanced if its first
# ceil(k/2) digits sum to the same value as its last ceil(k/2) digits.
# 
# So, for example, all palindromes are balanced, as is 13722.
# 
# Let T(n) be the sum of all balanced numbers less than 10^n. 
# Thus: T(1) = 45, T(2) = 540 and T(5) = 334795890.
# 
# Find T(47) mod 3^15.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap=47):
    # N[s][d] = number of d-digit numbers (possibly with leading zeroes)
    # whose digits sum to s
    N = [[0 for d in range(cap // 2 + 1)] for s in range(9 * (cap // 2) + 1)]
    # M[s][d] = number of d-digit numbers WITHOUT leading zeroes
    # whose digits sum to s
    M = [[0 for d in range(cap // 2 + 1)] for s in range(9 * (cap // 2) + 1)]
    N[0][0] = 1
    M[0][0] = 1
    for d in range(1, cap // 2 + 1):
        for s in range(9 * d + 1):
            N[s][d] += N[s][d-1]
            for digit in range(1, min(9, s) + 1):
                N[s][d] += N[s-digit][d-1]
                M[s][d] += N[s-digit][d-1]

    result = 45  # sum of all 1-digit numbers
    for k in range(1, cap // 2 + 1):  # Assume cap is odd
        for s in range(9 * k + 1):
            # mid
            result += 45 * 10 ** k * N[s][k] * M[s][k]
            for i in range(min(9, s) + 1):
                # low
                result += 11 * M[s][k] * i * (10 ** k - 1) // 9 * N[s-i][k-1]
                # high
                result += 101 * N[s][k] * i * (10 ** (k - 1) - 1) // 9 * (10 ** k) * M[s-i][k-1]
                # top
                result += 101 * N[s][k] * i * 10 ** (2 * k - 1) * N[s-i][k-1]
    return result % (3 ** 15)

start = time()
peresult(217, solve(), time() - start)
