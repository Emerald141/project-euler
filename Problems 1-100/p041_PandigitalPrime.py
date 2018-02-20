# We shall say that an n-digit number is pandigital if it makes
# use of all the digits 1 to n exactly once. For example, 2143
# is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# THEORY:
#
# The digits 1-9, and the digits 1-8, have a sum that is divisible by 3;
# therefore any number formed from a permutation of those digits will be
# divisible by 3. This means that the largest n-digit pandigital prime must have
# seven or fewer digits.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import isprime
from itertools import permutations

def solve():
    for digit_count in range(7, 0, -1):
        for perm_raw in permutations("7654321"[digit_count - 7:]):
            num = int(''.join(perm_raw))
            if isprime(num):
                return num
    print("Error: No pandigital primes found.")

if __name__ == "__main__":
    start = time()
    peresult(41, solve(), time() - start)
