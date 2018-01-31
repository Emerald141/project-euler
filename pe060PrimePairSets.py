# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
# primes and concatenating them in any order the result will always be
# prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set
# of four primes with this property.
# 
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

from time import time
from peresult import peresult
from primefns import primesbelow

def concat(num1, num2):
    tenpow = 10
    while tenpow <= num2:
        tenpow *= 10
    return num1 * tenpow + num2

def pe060(primelimit = 10000):
    start = time()
    primes = primesbelow(primelimit)
    primes = [3] + primes[3:]   # 2 and 5 will not be part of the set
    largeprimes = set(primesbelow(primelimit ** 2))
    result = 5 * primes[-1]
    pairs = [ [False for col in range(row)] for row in range(len(primes))]
    for p1 in range(len(primes)):
        for p2 in range(p1):
            if concat(primes[p1], primes[p2]) in largeprimes \
             and concat(primes[p2], primes[p1]) in largeprimes:
                pairs[p1][p2] = True
                for p3 in range(p2):
                    if pairs[p1][p3] and pairs[p2][p3]:
                        for p4 in range(p3):
                            if pairs[p1][p4] and pairs[p2][p4] \
                             and pairs[p3][p4]:
                                for p5 in range(p4):
                                    if pairs[p1][p5] and pairs[p2][p5] \
                                     and pairs[p3][p5] and pairs[p4][p5]:
                                        primetotal = primes[p1] + primes[p2] + \
                                         primes[p3] + primes[p4] + primes[p5]
                                        if primetotal < result:
                                            result = primetotal
    peresult(60, result, time() - start)

if __name__ == "__main__":
    pe060()
