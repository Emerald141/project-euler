# Let S(A) represent the sum of elements in set A of size n. We shall call it
# a special sum set if for any two non-empty disjoint subsets, B and C, the
# following properties are true:
# 
# S(B) ≠ S(C); that is, sums of subsets cannot be equal.
# If B contains more elements than C then S(B) > S(C).
# 
# For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set
# because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159,
# 161, 139, 158} satisfies both rules for all possible subset pair
# combinations and S(A) = 1286.
# 
# Using sets.txt (right click and "Save Link/Target As..."), a 4K text file
# with one-hundred sets containing seven to twelve elements (the two examples
# given above are the first two sets in the file), identify all the special
# sum sets, A_1, A_2, ..., A_k, and find the value of
# S(A_1) + S(A_2) + ... + S(A_k).

# THEORY:
#
# To examine the first condition, simply compare the largest disjoint subsets
# where one is one element larger than the other, but each element of the
# larger is less than each element of the smaller.
#
# To examine the second condition, compare all subsets with half the size
# of the set. If they have equal sum, then the non-overlapping subsets of
# these subsets have equal sum. All disjoint subset pairs of equal size
# can be implicitly compared in this way.

from time import time
from peresult import peresult
from itertools import combinations

def pe105():
    start = time()
    result = 0
    f = open("textfiles/p105_sets.txt")
    for line in range(100):
        numset = f.readline().rstrip('\n').split(',')
        for index in range(len(numset)):
            numset[index] = int(numset[index])
        numset = sorted(numset)
        n = len(numset)
        # Test for condition 1
        if sum(numset[:(n+1)//2]) <= sum(numset[(n+2)//2:]):
            continue
        # Test for condition 2
        sums = set()
        for subset in combinations(numset, n // 2):
            if sum(subset) in sums:
                break
            sums.add(sum(subset))
        else:
            result += sum(numset)
    peresult(105, result, time() - start)

if __name__ == "__main__":
    pe105()
