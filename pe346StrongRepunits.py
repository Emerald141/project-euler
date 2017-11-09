##The number 7 is special, because 7 is 111 written in base 2, and
##11 written in base 6 (i.e. 710 = 116_ = 111_2). In other words, 7
##is a repunit in at least two bases b > 1.
##
##We shall call a positive integer with this property a strong repunit.
##It can be verified that there are 8 strong repunits below 50:
##{1,7,13,15,21,31,40,43}. 
##Furthermore, the sum of all strong repunits below 1000 equals 15864.
##
##Find the sum of all strong repunits below 10**12.

from time import time
from peresult import peresult

def pe346(cap):
    start = time()
    repunits = set([1]) #1 is a repunit in all bases; special case
    base = 2
    while (1 + base + base ** 2 < cap):
        repunit = 1 + base + base ** 2
        max_exponent = 2
        while repunit < cap:
            repunits.add(repunit)
            max_exponent += 1
            repunit += base ** max_exponent
        base += 1
    result = sum(repunits)
    peresult(346, result, time() - start)

if __name__ == "__main__":
    pe346(10 ** 12)
