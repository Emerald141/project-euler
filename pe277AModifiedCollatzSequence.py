##A modified Collatz sequence of integers is obtained from a
##starting value a_1 in the following way:
##
##a_(n+1) = a_n/3 if an is divisible by 3.
##We shall denote this as a large downward step, "D".
##
##a_(n+1) = (4a_n + 2)/3 if an divided by 3 gives a remainder of 1.
##We shall denote this as an upward step, "U".
##
##a_(n+1) = (2a_n - 1)/3 if an divided by 3 gives a remainder of 2.
##We shall denote this as a small downward step, "d".
##
##The sequence terminates when some an = 1.
##
##Given any integer, we can list out the sequence of steps.
##For instance if a_1=231, then the sequence
##{a_n}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps "DdDddUUdDD".
##
##Of course, there are other sequences that begin with that same
##sequence "DdDddUUdDD....".
##For instance, if a_1=1004064, then the sequence is
##DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
##In fact, 1004064 is the smallest possible a1 > 10 ** 6 that begins
##with the sequence DdDddUUdDD.
##
##What is the smallest a_1 > 10 ** 15 that begins with the sequence
##"UDDDUdddDDUDDddDdDddDDUDDdUUDd"?

from time import time
from peresult import peresult
from fractions import Fraction

def pe277():
        start = time()
        #Reverse of the three steps:
        #D: 3*a
        #U: (3/4)a - (1/2)
        #d: (3/2)a + (1/2)
        varMult = Fraction(1, 1)
        addConst = Fraction(0, 1)
        sequence = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
        for ind in range(len(sequence) - 1, -1, -1):
                char = sequence[ind]
                if char == 'D':
                        varMult *= 3
                        addConst *= 3
                elif char == 'U':
                        varMult *= Fraction(3, 4)
                        addConst = addConst * Fraction(3, 4) - Fraction(1, 2)
                else:
                        varMult *= Fraction(3, 2)
                        addConst = addConst * Fraction(3, 2) + Fraction(1, 2)
        testedStart = 1
        vMNum = varMult.numerator
        aCNum = addConst.numerator
        denom = varMult.denominator  #which will also be addConst.denominator
        while (vMNum * testedStart + aCNum) % denom != 0:
                testedStart += 1
        while (varMult * testedStart + addConst) <= 10 ** 15:
                testedStart += denom
        result = (varMult * testedStart + addConst)
        peresult(277, result, time() - start)

if __name__ == "__main__":
        pe277()
