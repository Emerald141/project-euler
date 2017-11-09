##Work out the first ten digits of the sum of
##the following one-hundred 50-digit numbers.

from time import time
from peresult import peresult
from factorfns import factorsum

def pe21():
        start = time()
        result = 0
        for x in range(2, 10001):
                if x == factorsum(factorsum(x, True), True):
                        if x != factorsum(x, True):
                                result += x
        peresult(21, result, time() - start)
        
if __name__ == "__main__":
        pe21()
