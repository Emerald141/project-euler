# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
# The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
# difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their
# sum and difference are pentagonal and D = |Pk − Pj| is minimised;
# what is the value of D?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt
from itertools import count

def solve():
    penta_nums = [1, 5]
    for penta_creator in count(3):
        penta_nums.append(penta_creator * (3 * penta_creator - 1) // 2)
        for index in range(len(penta_nums) - 2, -1, -1):
            if is_penta(penta_nums[-1] + penta_nums[index]):
                if is_penta(penta_nums[-1] - penta_nums[index]):
                    return penta_nums[-1] - penta_nums[index]

def is_penta(num):
    if (1 + sqrt(1 + 24 * num)) / 6 % 1 == 0:
        return True
    return False

if __name__ == "__main__":
    start = time()
    peresult(44, solve(), time() - start)
