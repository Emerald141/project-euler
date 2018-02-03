# Let S(A) represent the sum of elements in set A of size n. We shall call
# it a special sum set if for any two non-empty disjoint subsets, B and C,
# the following properties are true:
#
# S(B) ≠ S(C); that is, sums of subsets cannot be equal.
# If B contains more elements than C then S(B) > S(C).
# If S(A) is minimised for a given n, we shall call it an optimum special
# sum set. The first five optimum special sum sets are given below.
#
# n = 1: {1}
# n = 2: {1, 2}
# n = 3: {2, 3, 4}
# n = 4: {3, 5, 6, 7}
# n = 5: {6, 9, 11, 12, 13}
#
# It seems that for a given optimum set, A = {a1, a2, ... , an}, the next
# optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the
# "middle" element on the previous row.
#
# By applying this "rule" we would expect the optimum set for n = 6 to be
# A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the
# optimum set, as we have merely applied an algorithm to provide a near
# optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25},
# with S(A) = 115 and corresponding set string: 111819202225.
#
# Given that A is an optimum special sum set for n = 7, find its set string.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import combinations

def solve():
    # Start from approximation rule given in problem
    base = [20] + [x + 20 for x in [11, 18, 19, 20, 22, 25]]
    # Iterate through displacements from approximation, up to 3 per element
    displacement = [-3, -3, -3, -3, -3, -3, -3]

    optimum_sum = 700   # Very loose upper bound
    result = "NotFound"

    while True:
        new_set = sorted([base[x] + displacement[x] for x in range(len(base))])
        # Test for condition 1 (and whether this set's total can be optimum)
        if sum(new_set) <= optimum_sum and sum(new_set[:4]) > sum(new_set[4:]):
            # Test for condition 2
            sums = set()
            for subset in combinations(new_set, 3):
                if sum(subset) in sums:
                    break
                sums.add(sum(subset))
            else:
                # Both conditions have been passed, and sum <= previous optimum
                optimum_sum = sum(new_set)
                result = ''.join(map(str, new_set))
        # Advance displacement
        if displacement[-1] < 3:
            displacement[-1] += 1
        else:
            index = len(displacement) - 1
            while index >= 0 and displacement[index] == 3:
                displacement[index] = -3
                index -= 1
            if index < 0:
                break   # All displacements within the range have been checked
            displacement[index] += 1
    return result

if __name__ == "__main__":
    start = time()
    peresult(103, solve(), time() - start)
