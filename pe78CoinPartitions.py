# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can be separated into piles
# in exactly seven different ways, so p(5)=7.
#
# OOOOO
# OOOO O
# OOO OO
# OOO O O
# OO OO O
# OO O O O
# O O O O O
#
# Find the least value of n for which p(n) is divisible by one million.

# THEORY:
#
# The pentagonal number theorem, proved by Euler, implies that
#   p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
# where the subtractive terms are the generalized pentagonal numbers,
# i.e. k(3k-1)/2 for k = 1, -1, 2, -2, 3, -3, ...

from time import time
from peresult import peresult

def pent_num(k):
    return k * (3 * k - 1) // 2

def pe78():
    start = time()
    pent_nums = [1, 2]
    k = 1
    partitions = [1, 1]
    n = 1
    while partitions[-1] != 0:
        n += 1
        if n > pent_nums[-1]:
            k += 1
            pent_nums.append(pent_num(k))
            pent_nums.append(pent_num(-k))
        partitions.append(0)
        for pent_num_index in range(len(pent_nums)):
            if pent_nums[pent_num_index] > n:
                break
            if pent_num_index % 4 < 2:
                partitions[-1] += partitions[n - pent_nums[pent_num_index]]
            else:
                partitions[-1] -= partitions[n - pent_nums[pent_num_index]]
        partitions[-1] %= 1000000
    peresult(78, n, time() - start)

if __name__ == "__main__":
    pe78()
