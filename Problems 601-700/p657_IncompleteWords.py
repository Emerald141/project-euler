# In the context of formal languages, any finite sequence of letters of a
# given alphabet S is called a word over S. We call a word incomplete if
# it does not contain every letter of S.
#
# For example, using the alphabet S = {a, b, c}, 'ab', 'abab' and '' (the
# empty word) are incomplete words over S, while 'acab' is a complete word
# over S.
#
# Given an alphabet S of m letters, we define I(m,n) to be the number of
# incomplete words over S with a length not exceeding n.
# For example, I(3,0) = 1, I(3,2) = 13 and I(3,4) = 79.
#
# Find I(10^7, 10^12). Give your answer modulo 1000000007.

# THEORY:
#
# This is just an inclusion-exclusion problem.
# If A(m,n) is the total number of words over an alphabet of m letters with
# a length not exceeding n, and C(x,y) is the binomial coefficient, then
# I(m,n) = C(m,m-1) A(m-1,n) - C(m,m-2) A(m-2,n) + C(m,m-3) A(m-3,n) - ...
#            +/- C(m,1) A(1,n) -/+ C(m,0) A(0,n).
# Also, A(m,n) = 1 + m + m^2 + ... + m^n.
# If m != 1, then A(m,n) = (m^(n+1) - 1) / (m - 1). Otherwise, A(1,n) = n+1.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

mod = 1000000007

def inv(x):
    # returns the modular inverse of x, for division purposes
    return pow(x, mod - 2, mod)

def A(m,n):
    if m == 1:
        return n + 1
    return ((pow(m, n+1, mod) - 1) * inv(m-1)) % mod

def solve(m = 10 ** 7, n = 10 ** 12):
    result = 0
    sign = 1
    coeff = 1
    for x in range(m-1, -1, -1):
        coeff = coeff * (x + 1) * inv(m - x) % mod
        result += sign * coeff * A(x, n)
        result %= mod
        sign *= -1
    return result

if __name__ == "__main__":
    start = time()
    peresult(657, solve(), time() - start)
