# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many
# letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in
# compliance with British usage.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    # Ones place digits, repeated except in cases of 11-19:
    ones = len("onetwothreefourfivesixseveneightnine") * 90
    # Last two digits in cases of 10-19:
    elevens = ( len("teneleventwelve") + 7 * len("teen") \
                    + len("thirfourfifsixseveneighnine") ) * 10
    # Tens place
    tens = ( len("twenthirforfifsixseveneighnine") + 8 * len("ty") ) * 100
    # The "and" before the last two digits, unless they're 00
    ands = len("and") * 99 * 9  # 99 times per hundredset, 9 hundredsets
    # Hundreds place
    hundreds = ( len("onetwothreefourfivesixseveneightnine") \
                    + 9 * len("hundred") ) * 100
    # And finally
    thousands = len("onethousand") #remember, no space!
    # Summing it all together:
    return ones + elevens + tens + ands + hundreds + thousands

if __name__ == "__main__":
    start = time()
    peresult(17, solve(), time() - start)
