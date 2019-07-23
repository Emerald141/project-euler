# It can be verified that there are 23 positive integers less than 1000 that
# are divisible by at least four distinct primes less than 100.
# 
# Find how many positive integers less than 10^16 are divisible by at least
# four distinct primes less than 100.

# THEORY:
#
# This is fundamentally an inclusion-exclusion problem, but it's made slightly
# more complicated by skipping the first few steps (since we don't want to
# count numbers divisible by only one, two, or three primes).
# As such we need to check how many times each overlapping area is counted
# at each step, and multiply the terms in each step to match.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow
from probability import choose
from matrixfns import matsolve

def subproduct(primes, indices):
    product = 1
    for index in indices:
        product *= primes[index]
    return product

def solve(cap = 10 ** 16):
    primes = primesbelow(100)
    
    mat = [ [0 for col in range(len(primes)-2)] for row in range(len(primes)-3)]
    for row in range(len(primes) - 3):
        for col in range(row + 1):
            mat[row][col] = choose(row + 4, col + 4)
        mat[row][-1] = 1
    multipliers = matsolve(mat)
    multipliers = list(map(int, multipliers))

    result = 0
    for length in range(4, len(primes)):
        indices = [i for i in range(length)]
        while True:
            term = (cap - 1) // (subproduct(primes, indices))
            result += multipliers[length - 4] * term
            # Move the rightmost index that we can right.
            # (except for the absolute rightmost index
            # if the term is zero; that would be pointless)
            if term != 0 and indices[-1] != len(primes) - 1:
                indices[-1] += 1
                continue
            for i in range(len(indices) - 2, -1, -1):
                if indices[i] + 1 != indices[i + 1]:
                    for j in range(len(indices) - 1, i - 1, -1):
                        indices[j] = indices[i] + j - i + 1
                    break
            else:
                # We've found all we can for this index count
                break
    return result

if __name__ == "__main__":
    start = time()
    peresult(268, solve(), time() - start)
