# The arithmetic sequence, 1487, 4817, 8147, in which each of
# the terms increases by 3330, is unusual in two ways: (i) each
# of the three terms are prime, and, (ii) each of the 4-digit
# numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-,
# or 3-digit primes, exhibiting this property, but there is one
# other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three
# terms in this sequence?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
        start = time()
        primes = primesbelow(10000)
        while primes[0] < 1000:
                del primes[0]
        for index1 in range(len(primes) - 1):
                prime1 = primes[index1]
                if prime1 == 1487:
                        continue
                for index2 in range(index1 + 1, len(primes)):
                        prime2 = primes[index2]
                        if not arePermutes(prime1, prime2):
                                continue
                        testprime = 2 * prime2 - prime1
                        if testprime in primes and arePermutes(prime1, testprime):
                                result = str(prime1) + str(prime2) + str(testprime)
                                break
                else:
                        continue
                break
        peresult(49, result, time() - start)

def arePermutes(num1, num2):
        list1 = sorted(str(num1))
        list2 = sorted(str(num2))
        return list1 == list2

if __name__ == "__main__":
        solve()
