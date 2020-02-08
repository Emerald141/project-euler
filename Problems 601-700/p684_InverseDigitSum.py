# Define s(n) to be the smallest number that has a digit sum of n.
# For example s(10)=19.
# Let S(k) = s(1) + ... + s(k). You are given S(20) = 1074.
#
# Further let f_i be the Fibonacci sequence defined by
# f_0 = 0, f_1 = 1 and f_i = f_{i−2} + f_{i−1} for all i >= 2.
#
# Find S(f_2) + ... + S(f_90). Give your answer modulo 1000000007.

# THEORY:
#
# For all n, all digits of s(n) except the leading digit will be 9.
# Hence s(9r+i) = i * 10^r + (10^r - 1) = (i+1) * 10^r - 1, for i < 9.
# So you can sum numbers in clusters of nine:
# s(9r) + s(9r + 1) + ... + s(9r + 8) = 45 * 10^r - 9.
# So, s(0) + ... + s(9r + 8) = 45 * (1 + 10 + ... + 10^r) - 9r - 9
#                            = 5 * (10^(r+1) - 1) - 9r - 9.
# If n = 9d + r, then the remaining terms are
# (0 + ... + r) * 10^d + (r + 1) * (10^d - 1)
# = r * (r + 1) / 2 * 10^d + (r + 1) * 10^d - r - 1.
# Summing these all together yields
# S(9d + r) = (5 * (r + 1)(1 + r/2)) * 10^d - n - 6.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def S(n, mod):
    d, r = n // 9, n % 9
    return ((5 + (r + 1 + (r * (r + 1) // 2))) * pow(10, d, mod) - n - 6) % mod

def solve(mod = 1000000007):
    fib_old = 0
    fib_new = 1
    result = 0
    for i in range(2, 91):
        print(i, fib_new)
        fib_old, fib_new = fib_new, fib_new + fib_old
        result += S(fib_new, mod)
    return result % mod

if __name__ == "__main__":
    start = time()
    peresult(684, solve(), time() - start)
