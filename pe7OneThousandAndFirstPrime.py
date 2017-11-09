##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
##we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?

from time import time
from peresult import peresult
from primefns import isprime

def pe7():
        start = time()
        iterator = 1
        primesfound = 0
        while primesfound < 10001:
                iterator += 1
                if isprime(iterator):
                        primesfound += 1
        peresult(7, iterator, time() - start)
        
if __name__ == "__main__":
        pe7()
