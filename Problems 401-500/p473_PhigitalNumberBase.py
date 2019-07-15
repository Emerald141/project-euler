# Let φ be the golden ratio: φ=(1+√5)/2.
# Remarkably it is possible to write every positive integer as a sum of powers
# of φ even if we require that every power of φ is used at most once in this
# sum.
# Even then this representation is not unique.
# We can make it unique by requiring that no powers with consecutive exponents
# are used and that the representation is finite.
# E.g: 2 = φ + φ^−2 and 3 = φ^2 + φ^−2
#
# To represent this sum of powers of φ we use a string of 0's and 1's with a
# point to indicate where the negative exponents start.
# We call this the representation in the phigital numberbase.
# So 1=1_φ, 2=10.01_φ, 3=100.01_φ and 14=100100.001001_φ.
# The strings representing 1, 2 and 14 in the phigital number base are
# palindromic, while the string representing 3 is not.
# (the phigital point is not the middle character).
#
# The sum of the positive integers not exceeding 1000 whose phigital
# representation is palindromic is 4345.
#
# Find the sum of the positive integers not exceeding 10^10 whose phigital
# representation is palindromic.

# THEORY:
#
# From experimental testing -- and this is probably based in theory but I didn't
# determine for sure -- the only non-1 phigital palindromes are linear combos of
#   φ^(2k+3) + φ^(2k) + φ^(-2k-1) + φ^(-2k-4)
# for positive integers k, and of 2 = φ + φ^-2.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt, log

def phi_mult(power):
    a, b = power[0], power[1]
    return ((a + 5 * b) // 2, (a + b) // 2)

def solve(cap = 10 ** 10):
    pows = [(2, 0)]  # Representing powers of phi. (m,n) means (m+n√5)/2.
    for i in range(int(log(cap, (1 + sqrt(5)) / 2)) + 2):
        pows.append(phi_mult(pows[-1]))
    terms = [2, cap+1]  # The second one there represents k=0 (impossible) and
                        # provides a buffer (can combine 2 with k=2 but not k=1)
    for k in range(1, (len(pows) - 3) // 2):
        terms.append((pows[2*k+3][0] + pows[2*k][0]
                       - pows[2*k+1][0] + pows[2*k+4][0]) // 2)
    # Now find all combinations of these terms under the cap where no two terms
    # are within two positions of each other.
    result = 1  # The oddball. Only palindrome without a point
    indices = [0]
    while len(indices) > 0:
        if indices[-1] >= len(terms):
            del(indices[-1])
            if len(indices) > 0:
                indices[-1] += 1
        else:
            new_pal = sum(terms[i] for i in indices)
            if new_pal <= cap:
                result += new_pal
                indices.append(indices[-1] + 3)
            else:
                if indices[-1] != 1:
                    del indices[-1]
                if len(indices) > 0:
                    indices[-1] += 1
    return result

if __name__ == "__main__":
    start = time()
    peresult(473, solve(10 ** 10), time() - start)
