# We call a natural number a duodigit if its decimal representation uses no
# more than two different digits. For example, 12, 110 and 33333 are
# duodigits, while 102 is not.
#
# It can be shown that every natural number has duodigit multiples.
# Let d(n) be the smallest (positive) multiple of the number n that happens to
# be a duodigit. For example, d(12)=12, d(102)=1122, d(103)=515,
# d(290)=11011010 and d(317)=211122.
#
# Let D(k) be the sum of d(n) from 1 to k.
# You are given D(110)=11047, D(150)=53312 and D(500)=29570988.
#
# Find D(50000). Give your answer in scientific notation rounded to
# 13 significant digits (12 after the decimal point). If, for example, we had
# asked for D(500) instead, the answer format would have been 2.957098800000e7.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def getmult(num, digs, mult_cap):
    queue = []
    saved = [mult_cap for x in range(num)]
    for dig in digs:
        if dig != 0:
            saved[dig] = dig
            queue.append(dig)
    while len(queue):
        if queue[0] * 10 < saved[0]:
            for dig in digs:
                x = queue[0] * 10 + dig
                if x < saved[x % num]:
                    saved[x % num] = x
                    queue.append(x)
        del queue[0]
    return saved[0]

def solve(cap = 50000):
    result = 0
    for num in range(1, cap + 1):
        if num % 100 == 0:
            print(num, time())
        if len(set(str(num))) <= 2:
            # num is already a duodigit
            result += num
            continue
        mult_cap = float("inf")
        for dig1 in range(0, 9):
            mult_cap = getmult(num, [dig1], mult_cap)
            for dig2 in range(dig1 + 1, 10):
                mult_cap = getmult(num, [dig1,dig2], mult_cap)
        result += mult_cap
    return result

if __name__ == "__main__":
    start = time()
    peresult(714, solve(), time() - start)
