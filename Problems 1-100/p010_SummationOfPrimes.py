##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
        start = time()
        result = sum(primesbelow(2000000))
        peresult(10, result, time() - start)
        
if __name__ == "__main__":
        solve()
