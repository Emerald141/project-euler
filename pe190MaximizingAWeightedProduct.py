##Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with
##x1 + x2 + ... + xm = m for which Pm = x1 * x2^2 * ... * xm^m is maximised.
##
##For example, it can be verified that [P10] = 4112
##([ ] is the integer part function).
##
##Find Σ[Pm] for 2 ≤ m ≤ 15.

from time import time
from peresult import peresult

def pe190():
    start = time()
    result = 0
    for x in range(2, 16):
        result += p(x)
    peresult(190, result, time() - start)

def p(m):
    product = 1
    for index in range(1, m+1):
        product *= ((2 * index)/(m+1))**index
    return int(product)

if __name__ == "__main__":
    pe190()
