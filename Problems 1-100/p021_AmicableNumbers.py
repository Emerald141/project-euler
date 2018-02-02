# Let d(n) be defined as the sum of proper divisors of n (numbers less than
# n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 10000):
    result = 0
    factor_sums = [0] + [1 for x in range(1, cap + 1)]
    for num in range(2, len(factor_sums)):
        for multiple in range(2 * num, len(factor_sums), num):
            factor_sums[multiple] += num
        if factor_sums[num] < num and factor_sums[factor_sums[num]] == num:
            result += num + factor_sums[num]
    return result

if __name__ == "__main__":
    start = time()
    peresult(21, solve(), time() - start)
