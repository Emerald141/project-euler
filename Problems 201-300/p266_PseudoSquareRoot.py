# The divisors of 12 are: 1, 2, 3, 4, 6 and 12.
# The largest divisor of 12 that does not exceed the square root of 12 is 3.
# We shall call the largest divisor of an integer n that does not exceed the
# square root of n the pseudo square root (PSR) of n.
# It can be seen that PSR(3102)=47.
#
# Let p be the product of the primes below 190.
# Find PSR(p) mod 10^16.

# THEORY:
#
# log(abcd) = log(a) + log(b) + log(c) + log(d)
# Kinda like a stacked blackjack: Add the logs of primes to get as close as
# you can to log(sqrt(p)) without going over.
# To make this easier, split the primes into two groups. Calculate all possible
# logs of numbers formed by multiplying primes in group 1, and in group 2.
# For each number in the first list, find the number in the second list which,
# when added to it, takes it as close as possible to log(sqrt(p)) without
# going over. Take the max of these.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow
from math import log

def log_combos(in_list, limit):
    # Save the primes used to construct, they'll be important later
    result = [(0, tuple())]
    for elem in in_list:
        result = result + [(c[0] + log(elem), c[1] + (elem,)) for c in result
                            if c[0] + log(elem) < limit]
    return sorted(result, key = lambda member: member[0])

def product(in_list):
    result = 1
    for elem in in_list:
        result *= elem
    return result

def solve(cap = 190):
    primes = primesbelow(cap)
    target = log(product(primes)) * 0.5
    combos_a = log_combos((p for p in primes[:len(primes) // 2]), target)
    combos_b = log_combos((p for p in primes[len(primes) // 2:]), target)
    best_answer = 1
    for a in combos_a:
        left, right = 0, len(combos_b) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if a[0] + combos_b[mid][0] < target:
                left = mid
            else:
                right = mid
        new_answer = product(a[1]) * product(combos_b[left][1])
        best_answer = max(best_answer, new_answer)
    return best_answer % (10 ** 16)

if __name__ == "__main__":
    start = time()
    peresult(266, solve(), time() - start)
