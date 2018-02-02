# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 2000000):
    return sum(primesbelow(cap))

if __name__ == "__main__":
    start = time()
    peresult(10, solve(), time() - start)
