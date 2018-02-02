##We shall say that an n-digit number is pandigital if it makes
##use of all the digits 1 to n exactly once. For example, 2143
##is a 4-digit pandigital and is also prime.
##
##What is the largest n-digit pandigital prime that exists?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from numassemble import numassemble
from primefns import isprime

def solve():
        start = time()
        #n != 9 because all permutations divisible by 3
        #n != 8 for the same reason
        #all the digits sum to a multiple of 3
        digits = [7 - x for x in range(7)]
        for a in digits:
                for b in digits:
                        if b != a:
                                for c in digits:
                                        if c not in [a, b]:
                                                for d in digits:
                                                        if d not in [a, b, c]:
                                                                for e in digits:
                                                                        if e not in [a, b, c, d]:
                                                                                for f in digits:
                                                                                        if f not in [a, b, c, d, e]:
                                                                                                for g in digits:
                                                                                                        if g not in [a, b, c, d, e, f]:
                                                                                                                num = numassemble(a, b, c, d, e, f, g)
                                                                                                                if isprime(num):
                                                                                                                        peresult(41, num, time() - start)
                                                                                                                        return
        #There's gotta be a better way to do this
        #Preferably, one that includes less indentation

if __name__ == "__main__":
        solve()
