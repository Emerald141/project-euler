##The number 3797 has an interesting property. Being prime itself,
##it is possible to continuously remove digits from left to right,
##and remain prime at each stage: 3797, 797, 97, and 7. Similarly
##we can work from right to left: 3797, 379, 37, and 3.
##
##Find the sum of the only eleven primes that are both truncatable
##from left to right and right to left.
##
##NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import time
from peresult import peresult
from primefns import isprime
from numassemble import numassemble

def pe37():
        start = time()
        result = 0
        count = 0
        primedigs = [1, 3, 7, 9]
        for a in primedigs + [2, 5]:
                for b in primedigs:
                        twonum = numassemble(a, b)
                        if isTruncPrime(twonum):
                                result += twonum
                                count += 1
                                if count == 11:
                                        peresult(37, result, time() - start)
                                        return
                        for c in primedigs:
                                threenum = numassemble(a, b, c)
                                if isTruncPrime(threenum):
                                        result += threenum
                                        count += 1
                                        if count == 11:
                                                peresult(37, result, time() - start)
                                                return
                                for d in primedigs:
                                        fournum = numassemble(a, b, c, d)
                                        if isTruncPrime(fournum):
                                                result += fournum
                                                count += 1
                                                if count == 11:
                                                        peresult(37, result, time() - start)
                                                        return
                                        for e in primedigs:
                                                fivenum = numassemble(a, b, c, d, e)
                                                if isTruncPrime(fivenum):
                                                        result += fivenum
                                                        count += 1
                                                        if count == 11:
                                                                peresult(37, result, time() - start)
                                                                return
                                                for f in primedigs:
                                                        sixnum = numassemble(a, b, c, d, e, f)
                                                        if isTruncPrime(sixnum):
                                                                result += sixnum
                                                                count += 1
                                                                if count == 11:
                                                                        peresult(37, result, time() - start)
                                                                        return

def isTruncPrime(lrtrunc):
        rltrunc = lrtrunc
        while rltrunc > 0:
                if not isprime(rltrunc):
                        return False
                rltrunc //= 10
        while lrtrunc > 0:
                if not isprime(lrtrunc):
                        return False
                if lrtrunc < 10:
                        return True
                lrtrunc = int(str(lrtrunc)[1:])

if __name__ == "__main__":
        pe37()
