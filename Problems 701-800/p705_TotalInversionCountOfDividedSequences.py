# The inversion count of a sequence of digits is the smallest number of
# adjacent pairs that must be swapped to sort the sequence.
# For example, 34214 has inversion count of 5:
# 34214→32414→23414→23144→21344→12344.
#
# If each digit of a sequence is replaced by one of its divisors a divided
# sequence is obtained.
# For example, the sequence 332 has 8 divided sequences:
# {332,331,312,311,132,131,112,111}.
#
# Define G(N) to be the concatenation of all primes less than N, ignoring
# any zero digit.
# For example, G(20)=235711131719.
#
# Define F(N) to be the sum of the inversion count for all possible divided
# sequences from the master sequence G(N).
# You are given F(20)=3312 and F(50)=338079744.
#
# Find F(10^8). Give your answer modulo 1000000007.

# THEORY:
#
# The number of inversions can be found by iterating along the string left to
# right, and for each digit, counting the number of elements greater than it
# on the left.
# Keep track of how many instances of each digit have been seen so far, and
# how many possible divided sequences there are so far.
# If I add a 4 to the end, then for every position to the left which contains
# a 6, 1/4 of the divided sequences have inversions there. So add
# 1/4 * (sixcount) * (divided sequence count) to the answer.
# Do this for all digit combinations.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 10 ** 8):
    mod = 1000000007
    inv = [0, 1] + [pow(d, mod - 2, mod) for d in range(2, 10)]
    is_prime = [False, False] + [True for x in range(2, cap)]
    seq_count = 1
    dig_count = [0 for dig in range(10)]
    divisors = [[0], [1], [1,2], [1,3], [1,2,4], [1,5], [1,2,3,6],
                [1,7], [1,2,4,8], [1,3,9]]
    multiplier = [[0 for p in range(10)] for dig in range(10)]
    for dig in range(1, 10):
        for d in divisors[dig]:
            for p in range(2, 10):
                for pd in divisors[p]:
                    if pd > d:
                        multiplier[dig][p] += 1
        for p in range(2, 10):
            multiplier[dig][p] *= inv[len(divisors[p])]
            multiplier[dig][p] %= mod
    result = 0
    for x in range(2, cap):
        if not is_prime[x]:
            continue
        for mult in range(x ** 2, cap, x):
            is_prime[mult] = False
        for dig_char in str(x):
            dig = int(dig_char)
            if dig == 0:
                continue
            term = 0
            for p in range(2, 10):
                term += dig_count[p] * multiplier[dig][p]
            result = (len(divisors[dig]) * result + seq_count * term) % mod
            seq_count = (seq_count * len(divisors[dig])) % mod
            dig_count[dig] += 1
    return result

if __name__ == "__main__":
    start = time()
    peresult(705, solve(), time() - start)
