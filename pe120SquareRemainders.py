##Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.
##
##For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 = 42 mod 49.
##And as n varies, so too will r, but for a = 7 it turns out that r_max = 42.
##
##For 3 <= a <= 1000, find the sum of r_max.

##As it turns out, (a-1)^n + (a+1) ^ n == 2na.
##Calculations below:
##
##        (a-1)^n + (a+1)^n
##        = (n choose 0)(a^n)((-1)^0) + (n choose 1)(a^(n-1))((-1)^1) + ... + (n choose n)(a^0)((-1)^n)
##            + (n choose 0)(a^n)(1^0) + (n choose 1)(a^(n-1))(1^1) + ... + (n choose n)(a^0)(1^n)
##        = 2(n choose 0)(a^n) + 2(n choose 2)(a^(n-2)) + 2(n choose 4)(a^(n-4)) + ...
##        n must be odd, because otherwise all terms would be divisible by n^2, and the remainder would be 0
##        = 2(n choose 0)(a^n) + 2(n choose 2)(a^(n-2)) + ... + 2(n choose n-1)(a)
##        The modulo of this with a^2 is
##        2(n choose n-1) a
##        = 2na
##
##The maximum remainder is thus (a-1)*a when a is odd, and (a-2)*a when a is even.

from time import time
from peresult import peresult

def pe120():
        start = time()
        total = 0
        for x in range(3, 1001):
                if x % 2 == 0:
                        total += (x - 2) * x
                else:
                        total += (x - 1) * x
        peresult(120, total, time() - start)

if __name__ == "__main__":
        pe120()
