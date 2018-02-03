# A perfect number is a number for which the sum of its
# proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors
# is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two
# abundant numbers is 24. By mathematical analysis, it can be
# shown that all integers greater than 28123 can be written as
# the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is
# known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be
# written as the sum of two abundant numbers.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 28123):
    abundants = []
    factor_sums = [0] + [1 for x in range(cap + 1)]
    for num in range(2, len(factor_sums)):
        for multiple in range(2 * num, len(factor_sums), num):
            factor_sums[multiple] += num
        if factor_sums[num] > num:
            abundants.append(num)
    nonsums = [True for x in range(cap + 1)]
    for large in range(1, len(abundants)):
        for small in range(large + 1):
            if abundants[large] + abundants[small] > cap:
                break
            nonsums[abundants[large] + abundants[small]] = False
    result = 0
    for index in range(len(nonsums)):
        if nonsums[index]:
            result += index
    return result

if __name__ == "__main__":
    start = time()
    peresult(23, solve(), time() - start)
