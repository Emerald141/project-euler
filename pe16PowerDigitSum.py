##215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
##What is the sum of the digits of the number 2 ** 1000?

from time import time
from peresult import peresult
from digitfns import digitsum

def pe16():
        start = time()
        result = digitsum(2 ** 1000)
        peresult(16, result, time() - start)

if __name__ == "__main__":
        pe16()
