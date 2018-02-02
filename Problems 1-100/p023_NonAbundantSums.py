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
from factorfns import factorsum

def solve():
        start = time()
        ablist = [] #as in list of "ab"undants, not as in discriminatory!!!
        for x in range(1, 28123):
                if factorsum(x, True) > x:
                        ablist.append(x)
        nonsums = [True for x in range(28124)]
        for largerab in range(len(ablist)):
                for smallerab in range(largerab + 1):
                        if ablist[largerab] + ablist[smallerab] > 28123:
                                break
                        nonsums[ablist[largerab] + ablist[smallerab]] = False
        result = 0
        for index in range(len(nonsums)):
                if nonsums[index]:
                        result += index
        peresult(23, result, time() - start)

if __name__ == "__main__":
        solve()
