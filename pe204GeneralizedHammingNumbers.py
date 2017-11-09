##A Hamming number is a positive number which has no prime factor larger than 5.
##So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
##There are 1105 Hamming numbers not exceeding 10**8.
##
##We will call a positive number a generalised Hamming number of type n,
##if it has no prime factor larger than n.
##Hence the Hamming numbers are the generalised Hamming numbers of type 5.
##
##How many generalised Hamming numbers of type 100 are there which don't
##exceed 10**9?

from time import time
from peresult import peresult
from primefns import primesbelow

def pe204(primelimit, hamminglimit):
    start = time()
    primes = primesbelow(primelimit + 1)
    exponents = [0 for x in range(len(primes))]
    index = 0
    hamming = 1
    count = 0
    while True:
        if hamming > hamminglimit:
            hamming //= primes[index] ** exponents[index]
            exponents[index] = 0
            if index == 0:
                break
            else:
                exponents[index - 1] += 1
                hamming *= primes[index - 1]
                index -= 1
        else:
            if index == len(primes) - 1:
                count += 1
                exponents[index] += 1
                hamming *= primes[index]
            else:
                index += 1
    peresult(204, count, time() - start)

if __name__ == "__main__":
    pe204(100, 10**9)
