# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly
# we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
    primes = set(primesbelow(10 ** 6))

    def is_trunc_prime(num):
        # Trim from the right
        right_trim = num // 10
        while right_trim > 0:
            if right_trim not in primes:
                return False
            right_trim //= 10
        # Trim from the left
        ten_pow = 10
        while ten_pow * 10 < num:
            ten_pow *= 10
        while num > 0:
            if num not in primes:
                return False
            num %= ten_pow
            ten_pow //= 10
        return True

    count = 0
    total = 0
    for prime in primes:
        if is_trunc_prime(prime):
            count += 1
            total += prime
            if count == 15:  # counting 2, 3, 5, and 7...
                return total - 17  # ...and then uncounting them
    print("Error: Cap on primes too low")

if __name__ == "__main__":
    start = time()
    peresult(37, solve(), time() - start)
