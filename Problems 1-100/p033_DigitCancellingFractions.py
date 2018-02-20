# The fraction 49/98 is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly
# believe that 49/98 = 4/8, which is correct, is obtained by
# cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator
# and denominator.
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from fractions import Fraction

def solve():
    start = time()
    # Numerator and denominator of the product of the four fractions
    grand_numer = 1
    grand_denom = 1
    # Iterate through
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                numer = 10 * a + b
                if numer == 0:
                    continue
                # Fraction 1: ab / bc
                denom1 = 10 * b + c
                if numer < denom1 and numer / denom1 == a / c:
                    grand_numer *= a
                    grand_denom *= c
                # Fraction 2: ab / ca
                denom2 = 10 * c + a
                if numer < denom2 and numer / denom2 == b / c:
                    grand_numer *= b
                    grand_denom *= c
    return Fraction(grand_numer, grand_denom).denominator

if __name__ == "__main__":
    start = time()
    peresult(33, solve(), time() - start)
