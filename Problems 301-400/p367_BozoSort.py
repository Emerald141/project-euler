# Bozo sort, not to be confused with the slightly less efficient bogo sort,
# consists out of checking if the input sequence is sorted and if not swapping
# randomly two elements. This is repeated until eventually the sequence
# is sorted.
#
# If we consider all permutations of the first 4 natural numbers as input the
# expectation value of the number of swaps, averaged over all 4! input
# sequences is 24.75.
# The already sorted sequence takes 0 steps.
#
# In this problem we consider the following variant on bozo sort.
# If the sequence is not in order we pick three elements at random and shuffle
# these three elements randomly.
# All 3!=6 permutations of those three elements are equally likely.
# The already sorted sequence will take 0 steps.
# If we consider all permutations of the first 4 natural numbers as input the
# expectation value of the number of shuffles, averaged over all 4! input
# sequences is 27.5.
# Consider as input sequences the permutations of the first 11 natural numbers.
# Averaged over all 11! input sequences, what is the expected number of
# shuffles this sorting algorithm will perform?
#
# Give your answer rounded to the nearest integer.

# THEORY:
#
# The 11! permutations of the first 11 natural numbers can be divided into
# subsets based on the cycle structure of the permutation.
# For instance, (1,2,6,11,7,3)(4,5)(8,9)(10) and (10,4,2,6,11,3)(1,7)(5,8)(9)
# both have cyclic structure [6, 2, 2, 1].
# There's only a few dozen possible cycle structues for 11 elements,
# so the transition matrix is easier to compute.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matsolve
from itertools import permutations, combinations
from math import factorial

# Find all partitions of a non-negative integer n
def get_partitions(n, cap=11):
    if n == 0:
        return [[]]
    ret = []
    for i in range(1, min(n, cap) + 1):
        for x in get_partitions(n-i, i):
            ret.append([i] + x)
    return ret

# Find the index in a list of partitions corresponding to the cycle
# structure of a given permutation
def get_index(perm, partitions):
    found = [False for i in range(len(perm))]
    cycles = []
    for start in range(len(perm)):
        if not found[start]:
            new_cycle = 0
            i = start
            while not found[i]:
                new_cycle += 1
                found[i] = True
                i = perm[i]
            cycles.append(new_cycle)
    return partitions.index(tuple(sorted(cycles, reverse=True)))

# Find some permutation with a given cycle structure.
def get_template(partition):
    ret = [0 for i in range(sum(partition))]
    i = 0
    for cycle in partition:
        remaining = cycle
        start = i
        while remaining > 1:
            ret[i] = i+1
            remaining -= 1
            i += 1
        ret[i] = start
        i += 1
    return ret

def solve(n = 11):
    partitions = [tuple(x) for x in get_partitions(n)]
    m = len(partitions)
    mat = [ [0 for col in range(m + 1)] for row in range(m)]
    for row in range(m):
        template = get_template(partitions[row])
        if row == 0:
            mat[row][row] = 1
            continue
        mat[row][row] = n * (n-1) * (n-2)
        mat[row][-1] = n * (n-1) * (n-2)
        for c in combinations(range(n), 3):
            for p in permutations(range(3)):
                new_perm = template[:]
                for i in range(3):
                    new_perm[c[p[i]]] = template[c[p[p[i]]]]
                
                mat[row][get_index(new_perm, partitions)] -= 1
    expected = matsolve(mat)
    # Now that we've found the expected steps from each pattern,
    # how many permutations are of each pattern?
    result = 0
    for j in range(m):
        partition = partitions[j]
        term = 1
        remaining = n
        for index in range(len(partition)):
            i = partition[index]
            term *= factorial(remaining) // factorial(remaining - i) // i
            remaining -= i
            if index >= 1 and partition[index] == partition[index - 1]:
                streak += 1
            else:
                streak = 1
            term //= streak
        result += expected[j] * term
    return round(result / factorial(n))

if __name__ == "__main__":
    start = time()
    peresult(367, solve(), time() - start)
