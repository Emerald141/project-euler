##The sum of the squares of the first ten natural numbers is,
##
##1^2 + 2^2 + ... + 10^2 = 385
##The square of the sum of the first ten natural numbers is,
##
##(1 + 2 + ... + 10)^2 = 55^2 = 3025
##Hence the difference between the sum of the squares of the first
##ten natural numbers and the square of the sum is 3025 − 385 = 2640.
##
##Find the difference between the sum of the squares of the first
##one hundred natural numbers and the square of the sum.

from time import time
from peresult import peresult

def pe6():
        start = time()
        lower = 0
        numsum = 0
        for x in range(1, 101):
                lower += x ** 2
                numsum += x
        peresult(6, numsum ** 2 - lower, time() - start)
        
if __name__ == "__main__":
        pe6()
