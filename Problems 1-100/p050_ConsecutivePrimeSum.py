# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 1000000):
    primes = primesbelow(cap)
    # Find max number of primes that, when concatenated, sum to less than cap
    initial_prime_sum = 0
    end_index = -1
    while initial_prime_sum + primes[end_index + 1] < cap:
        end_index += 1
        initial_prime_sum += primes[end_index]
    if initial_prime_sum in primes:
        return initial_prime_sum  # This probably won't happen, but safety first
    for length in range(end_index + 1, 0, -1):
        # initial_prime_sum is the max sum below cap of primes with given length
        start_index = end_index - length + 1
        while initial_prime_sum - primes[start_index] + primes[end_index] < cap:
            initial_prime_sum += -primes[start_index] + primes[end_index]
            end_index += 1
            start_index += 1
        # Add a prime to the beginning and trim a prime from the end
        # Do this until either we run out of primes or the total is prime
        new_prime_sum = initial_prime_sum
        new_end_index = end_index
        new_start_index = start_index
        while new_prime_sum not in primes and new_start_index > 0:
            new_start_index -= 1
            new_end_index -= 1
            new_prime_sum += primes[new_start_index] - primes[new_end_index + 1]
        if new_prime_sum in primes:
            return new_prime_sum
        # No chains of given length sum to a prime. Trim one from the start
        initial_prime_sum -= primes[start_index]

if __name__ == "__main__":
    start = time()
    peresult(50, solve(10 ** 6), time() - start)
