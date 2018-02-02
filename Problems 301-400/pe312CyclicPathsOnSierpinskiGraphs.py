##- A Sierpiński graph of order-1 (S_1) is an equilateral triangle.
##- S_(n+1) is obtained from S_n by positioning three copies of S_n so that
##every pair of copies has one common corner.
##
##Let C(n) be the number of cycles that pass exactly once through all the
##vertices of S_n.
##For example, C(3) = 8 because eight such cycles can be drawn on S_3.
##
##It can also be verified that:
##C(1) = C(2) = 1
##C(5) = 71328803586048
##C(10 000) mod 10^8 = 37652224
##C(10 000) mod 13^8 = 617720485
##
##Find C(C(C(10 000))) mod 13^8.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from totient import totient

def powermod(base, exponent, mod):
    result = 1
    currentTerm = base
    while exponent > 0:
        if exponent % 2 == 1:
            result *= currentTerm
            result %= mod
        currentTerm **= 2
        currentTerm %= mod
        exponent //= 2
    return result

def solve():
    start = time()
    # C(n) = 8 * 12^( 1/2 * (3 ^ (n - 2) - 3))
    totients = [totient(13 ** 8)]
    for i in range(7):
        if i % 3 == 0:
            totients.append(2 * totients[-1])
        else:
            totients.append(totient(totients[-1]))
    exponent = 9998
    for stage in range(len(totients)-1, -1, -1):
        if stage % 3 == 1:
            exponent = powermod(3, exponent, totients[stage]) - 3
        elif stage % 3 == 0:
            if exponent % 2 == 1: print("Uh oh")
            exponent //= 2
        else:
            exponent = 8 * powermod(12, exponent, totients[stage]) - 2
        exponent %= totients[stage]
    result = 8 * powermod(12, exponent, 13 ** 8)
    result %= 13 ** 8
    peresult(312, result, time() - start)

if __name__ == "__main__":
    solve()
