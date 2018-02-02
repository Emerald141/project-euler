##We shall say that an n-digit number is pandigital if it makes use
##of all the digits 1 to n exactly once; for example, the 5-digit
##number, 15234, is 1 through 5 pandigital.
##
##The product 7254 is unusual, as the identity, 39 × 186 = 7254,
##containing multiplicand, multiplier, and product is 1 through 9 pandigital.
##
##Find the sum of all products whose multiplicand/multiplier/product
##identity can be written as a 1 through 9 pandigital.
##
##HINT: Some products can be obtained in more than one way so be sure
##to only include it once in your sum.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        digits = [x for x in range(1, 10)]
        result = 0
        for a in digits:
                for b in digits:
                        if b != a:
                                for c in digits:
                                        if c not in [a, b]:
                                                for d in digits:
                                                        if d not in [a, b, c]:
                                                                dividendadded = False
                                                                for e in digits:
                                                                        if dividendadded:
                                                                                break
                                                                        if e not in [a, b, c, d]:
                                                                                for f in digits:
                                                                                        if f not in [a, b, c, d, e]:
                                                                                                # abcd // ef == ghi
                                                                                                dividend = 1000 * a + 100 * b + 10 * c + d
                                                                                                divisor = 10 * e + f
                                                                                                quotient = dividend / divisor
                                                                                                if quotient >= 1000 or quotient % 1 != 0:
                                                                                                        continue
                                                                                                g = quotient // 100
                                                                                                h = quotient // 10 % 10
                                                                                                i = quotient // 1 % 10
                                                                                                if len(set([a, b, c, d, e, f, g, h, i])) != 9 or 0 in [g, h, i]:
                                                                                                        continue
                                                                                                result += dividend
                                                                                                dividendadded = True
                                                                                                break
                                                                if not dividendadded:
                                                                        for e in digits:
                                                                                if e not in [a, b, c, d]:
                                                                                        # abcd // e == fghi
                                                                                        dividend = 1000 * a + 100 * b + 10 * c + d
                                                                                        quotient = dividend / e
                                                                                        if quotient < 1000 or quotient % 1 != 0:
                                                                                                continue
                                                                                        f = quotient // 1000
                                                                                        g = quotient // 100 % 10
                                                                                        h = quotient // 10 % 10
                                                                                        i = quotient // 1 % 10
                                                                                        prevlist = [a, b, c, d, e]
                                                                                        if len(set([a, b, c, d, e, f, g, h, i])) != 9 or quotient % 1 != 0 or 0 in [f, g, h, i]:
                                                                                                continue
                                                                                        result += dividend
                                                                                        break
        peresult(32, result, time() - start)

if __name__ == "__main__":
        solve()
                                                                                                
