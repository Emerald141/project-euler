##The fraction 49/98 is a curious fraction, as an inexperienced
##mathematician in attempting to simplify it may incorrectly
##believe that 49/98 = 4/8, which is correct, is obtained by
##cancelling the 9s.
##
##We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
##
##There are exactly four non-trivial examples of this type of fraction,
##less than one in value, and containing two digits in the numerator
##and denominator.
##
##If the product of these four fractions is given in its lowest common
##terms, find the value of the denominator.

from time import time
from peresult import peresult
from fractions import Fraction

def pe33():
        start = time()
        grandnumer = 1
        granddenomer = 1
        for a in range(10):
                for b in range(10):
                        for c in range(10):
                                numer = 10 * a + b
                                if numer == 0:
                                        continue
                                denomer1 = 10 * b + c
                                if b != 0 and c != 0 and numer < denomer1:
                                        if numer / denomer1 == a / c:
                                                grandnumer *= a
                                                granddenomer *= c
                                denomer2 = 10 * c + a
                                if a != 0 and c != 0 and numer < denomer2:
                                        if numer / denomer2 == b / c:
                                                grandnumer *= b
                                                granddenomer *= c
        result = Fraction(grandnumer, granddenomer).denominator
        peresult(33, result, time() - start)

if __name__ == "__main__":
        pe33()
