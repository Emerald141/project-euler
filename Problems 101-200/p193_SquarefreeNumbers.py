# A positive integer n is called squarefree, if no square of a prime
# divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not
# 4, 8, 9, 12.
#
# How many squarefree numbers are there below 2^50?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow
from itertools import count
from math import sqrt

def listprod(source, indices):
    result = 1
    for i in indices:
        result *= source[i]
    return result

def solve():
    cap = 2 ** 50
    result = cap
    primes = primesbelow(int(sqrt(cap)) + 1)
    for i in range(len(primes)):
        primes[i] = primes[i] ** 2
    primes.append(cap+1)
    # So technically 'primes' is inaccurate but whatever
    for primecount in count(1):
        indices = list(range(primecount))
        term = listprod(primes, indices)
        if term > cap:
            return result
        while True:
            if term <= cap:
                result += (cap // term) * pow(-1, primecount)
                term //= primes[indices[-1]]
                term *= primes[indices[-1] + 1]
                indices[-1] += 1
            else:
                # Are there any nonconsecutive indices?
                if indices[-1] == indices[0] + primecount - 1:
                    break
                # If so, advance the last nonconsecutive index.
                for i in range(primecount - 2, -1, -1):
                    if indices[i] != indices[i+1] - 1:
                        indices[i] += 1
                        for j in range(i+1, primecount):
                            indices[j] = indices[j-1] + 1
                        term = listprod(primes, indices)
                        break

if __name__ == "__main__":
    start = time()
    peresult(193, solve(), time() - start)
