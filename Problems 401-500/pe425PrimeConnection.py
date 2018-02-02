##Two positive numbers A and B are said to be connected (denoted by "A ↔ B")
##if one of these conditions holds:
##(1) A and B have the same length and differ in exactly one digit; for
##example, 123 ↔ 173.
##(2) Adding one digit to the left of A (or B) makes B (or A); for example,
##23 ↔ 223 and 123 ↔ 23.
##
##We call a prime P a 2's relative if there exists a chain of connected
##primes between 2 and P and no prime in the chain exceeds P.
##
##For example, 127 is a 2's relative. One of the possible chains is shown below:
##2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127
##However, 11 and 103 are not 2's relatives.
##
##Let F(N) be the sum of the primes ≤ N which are not 2's relatives.
##We can verify that F(10^3) = 431 and F(10^4) = 78728.
##
##Find F(10^7).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap):
    start = time()
    print("Note: This one takes just a LITTLE over a minute, but since it's" \
          + " pretty close and in Python, I'm calling it good enough.")
    rawPrimes = primesbelow(cap)
    maxLink = dict() #Largest element in chain from 2 to prime (minimized)
    for prime in rawPrimes:
        maxLink[prime] = cap + 1
    maxLink[2] = 2
    currentPrimes = {2}
    while len(currentPrimes) > 0:
        newPrimes = set()
        for prime in currentPrimes:
            #Replace a digit
            clone = prime
            power = 0
            while clone > 0:
                currentDigit = clone % 10
                #Decrease a digit
                for diff in range(1, currentDigit + 1):
                    possibleNew = prime - (diff * (10 ** power))
                    if possibleNew in maxLink \
                       and maxLink[prime] < maxLink[possibleNew]:
                        maxLink[possibleNew] = max(possibleNew, maxLink[prime])
                        newPrimes.add(possibleNew)
                #Increase a digit
                for diff in range(1, 10 - currentDigit):
                    possibleNew = prime + (diff * (10 ** power))
                    if possibleNew in maxLink \
                       and maxLink[possibleNew] > max(possibleNew, \
                                                      maxLink[prime]):
                        maxLink[possibleNew] = max(possibleNew, maxLink[prime])
                        newPrimes.add(possibleNew)
                clone //= 10
                power += 1
            #Add a digit on the left
            for dig in range(1, 10):
                possibleNew = ((10 ** power) * dig) + prime
                if possibleNew in maxLink \
                   and maxLink[possibleNew] > max(possibleNew, \
                                                  maxLink[prime]):
                    maxLink[possibleNew] = max(possibleNew, maxLink[prime])
                    newPrimes.add(possibleNew)
        currentPrimes = newPrimes
    result = 0
    for prime in maxLink.keys():
        if maxLink[prime] > prime:
            result += prime
    peresult(425, result, time() - start)

if __name__ == "__main__":
    solve(10 ** 7)
