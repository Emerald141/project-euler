# A natural number, N, that can be written as the sum and product of a given
# set of at least two natural numbers, {a1, a2, ... , ak} is called a
# product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
# 
# For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
# 
# For a given set of size, k, we shall call the smallest N with this property
# a minimal product-sum number. The minimal product-sum numbers for sets of
# size k = 2, 3, 4, 5, and 6 are as follows.
# 
# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
# 
# Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is
# 4+6+8+12 = 30; note that 8 is only counted once in the sum.
# 
# In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is
# {4, 6, 8, 12, 15, 16}, the sum is 61.
# 
# What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

# THEORY:
# 
# For given k, we only have to check numbers up to 2k, because
# where the 1 term is repeated k-2 times,
# 1 + ... + 1 + 2 + k = 1 * ... * 1 * 2 * k = 2k.
# 
# If we iterate through lists of non-1 factors and set n equal to the product
# of these factors, we can find the number of 1 factors as n minus the sum of
# its non-1 factors, which leads immediately to the total number of factors.
# We can keep a running list of the smallest n for each number of factors.
# 
# This program iterates through lists of non-1 factors by using an array to
# simulate a nested for loop. Each term is always larger than or equal to the
# term preceding it. If the last term gets too large, a previous term is
# incremented, and all following terms are set equal to it. If all terms get too
# large, a new term is added, and all terms are set to 2. This continues until
# even the product of 2's gets too large.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def product(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

def solve(cap = 12000):
    start = time()
    ps_nums = [0, 0] + [ cap * 2 + 1 for k in range(cap - 1) ]
    factors = [2, 2]
    while 2 ** (len(factors) - 1) <= cap:
        num = product(factors)
        term_count = num - sum(factors) + len(factors)
        if num > 2 * cap or term_count > cap:   # Last term is now too large
            for previous_index in range(len(factors) - 2, -1, -1):
                if factors[previous_index] < factors[-1] - 1:
                    factors[previous_index] += 1
                    for following_index in range(previous_index + 1, len(factors)):
                        factors[following_index] = factors[previous_index]
                    break
            else:
                factors = [2 for index in range(len(factors) + 1)]
        else:   # Potential hit for k = term_count
            if num < ps_nums[term_count]:
                ps_nums[term_count] = num
            factors[-1] += 1
    result = sum(set(ps_nums))
    peresult(88, result, time() - start)

if __name__ == "__main__":
    solve()
