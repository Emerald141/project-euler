# For any N, let f(N) be the last five digits before the trailing zeroes in N!.
# For example,
#
# 9! = 362880 so f(9)=36288
# 10! = 3628800 so f(10)=36288
# 20! = 2432902008176640000 so f(20)=17664
#
# Find f(1,000,000,000,000)

# THEORY:
#
# Let the "semi-factorial" N? of N be the product of all the positive integers
# less than or equal to N which are not divisible by 2 or 5.
# Ex. 20? = 1 * 3 * 7 * 9 * 11 * 13 * 17 * 19 = 8729721.
#
# Then N! = 2^(N/2) * 5^(N/5) * N? * (N/2)! * (N/5)! / (N/10)!
# Let R be the total number of factors of 2 in N!, and let Q be the total
# number of factors of 5 in N!.
# Expanding the above equation out further yields
# N! = 2^R * 5^Q * Product of (N/(2^i * 5^j))? for i, j nonnegative.
# The part of N! before the trailing zeroes is equal to this divided by 10^Q,
# i.e. 2^(R-Q) * Product of (N/(2^i * 5^j))? for i, j nonnegative.
#
# Let M = 100,000?.
# Then the last five digits of (k * 100,000 + x)? are also the last five digits
# of M^k * x?.

from time import time
from itertools import count
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(N = 10 ** 12, mod = 10 ** 5):
    # Step 1: Find R and Q, then find the last five digits of 2^(R-Q).
    temp_N = N
    two_powers = 0
    while temp_N > 0:
        two_powers += temp_N // 2
        temp_N //= 2
    temp_N = N
    five_powers = 0
    while temp_N > 0:
        five_powers += temp_N // 5
        temp_N //= 5
    result = pow(2, two_powers - five_powers, mod)
    # Step 2: Find the last five digits of x? for x between 0 and 100,000.
    semi_factorials = [1 for x in range(mod)]
    for x in range(1, mod):
        if x % 2 != 0 and x % 5 != 0:
            semi_factorials[x] = (semi_factorials[x-1] * x) % mod
        else:
            semi_factorials[x] = semi_factorials[x-1]
    large_semi = semi_factorials[-1]  # M
    # Step 3: Multiply the result by (N/(2^i * 5^j))? for nonnegative i and j
    for i in count():
        if 2 ** i > N:
            break
        for j in count():
            if 2 ** i * 5 ** j > N:
                break
            term_input = N // (2 ** i * 5 ** j)
            result *= pow(large_semi, term_input // mod, mod)
            result *= semi_factorials[term_input % mod]
            result %= mod
    return result

if __name__ == "__main__":
    start = time()
    peresult(160, solve(), time() - start)
