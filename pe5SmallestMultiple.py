##2520 is the smallest number that can be divided by each of the numbers
##from 1 to 10 without any remainder.
##
##What is the smallest positive number that is evenly divisible by all
##of the numbers from 1 to 20?

from time import time
from peresult import peresult
from factorfns import factorizationpow

def pe5():
        start = time()
        largedict = dict()
        for x in range(2, 21):
                smalldict = factorizationpow(x)
                for key in smalldict.keys():
                        if key in largedict.keys() and largedict[key] > smalldict[key]:
                                continue
                        else:
                                largedict[key] = smalldict[key]
        result = 1
        for key in largedict.keys():
                result *= key ** largedict[key]
        peresult(5, result, time() - start)
        
if __name__ == "__main__":
        pe5()
