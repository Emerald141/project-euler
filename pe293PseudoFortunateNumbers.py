##An even positive integer N will be called admissible, if it is a power
##of 2 or its distinct prime factors are consecutive primes.
##The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.
##
##If N is admissible, the smallest integer M > 1 such that N+M is prime,
##will be called the pseudo-Fortunate number for N.
##
##For example, N=630 is admissible since it is even and its distinct prime
##factors are the consecutive primes 2,3,5 and 7.
##The next prime number after 631 is 641; hence, the pseudo-Fortunate
##number for 630 is M=11.
##It can also be seen that the pseudo-Fortunate number for 16 is 3.
##
##Find the sum of all distinct pseudo-Fortunate numbers for admissible
##numbers N less than 10^9.

from time import time
from peresult import peresult
from primefns import primesbelow

def pe293():
    start = time()
    primes = primesbelow(int(10 ** 4.5) + 1)
    exponents = []
    admissible = 1
    pointer = 0
    while admissible * primes[pointer] < 10 ** 9:
        admissible *= primes[pointer]
        exponents.append(1)
        pointer += 1
    pseudos = set()
    while len(exponents) > 0:
        #Add the pseudo-Fortunate number for this admissible number
        pseudo = 2
        pseudoIsGood = False
        while not pseudoIsGood:
            for prime in primes:
                if (admissible + pseudo) % prime == 0:
                    pseudo += 1
                    break
                if prime ** 2 > admissible + pseudo or prime == primes[-1]:
                    pseudos.add(pseudo)
                    pseudoIsGood = True
                    break
        #Find the next admissible number
        admissible *= primes[0]
        exponents[0] += 1
        pointer = 0
        while admissible >= 10 ** 9:
            if pointer == len(exponents) - 1:
                admissible //= primes[pointer] ** exponents[pointer]
                del exponents[pointer]
                break
            else:
                admissible //= primes[pointer] ** (exponents[pointer] - 1)
                exponents[pointer] = 1
                admissible *= primes[pointer + 1]
                exponents[pointer + 1] += 1
                pointer += 1
    result = sum(pseudos)
    peresult(293, result, time() - start)

if __name__ == "__main__":
    pe293()
