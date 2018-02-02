# We define a simber to be a positive integer in which any odd digit,
# if present, occurs an odd number of times, and any even digit, if
# present, occurs an even number of times.
# 
# For example, 141221242 is a 9-digit simber because it has three 1's,
# four 2's and two 4's.
# 
# Let Q(n) be the count of all simbers with at most n digits.
# 
# You are given Q(7) = 287975 and Q(100) mod 1 000 000 123 = 123864868.
# 
# Find (sum_{1<=u<=39} Q(2^u)) mod 1 000 000 123.

# THEORY:
#
# If we start building the number from the left, this becomes a dynamic
# programming problem with a finite set of states.
# Define a digit as "unbalanced" if it must appear an odd
# number of times farther down in order for the number to be a simber
# (i.e. if even, it's appeared an odd number of times, or vice versa).
# Then each state is defined by two variables: X, the number of unbalanced
# digits, and Y, the number of odd digits that have appeared thus far.
# (We have to include Y because each odd digit is NOT unbalanced by
# its first appearance.)
#
# Y ranges from 0 to 5, and X ranges from 0 to 5+Y.
# There's also one more state for an as-yet-empty number.
# There are therefore 52 states.
#
# At any state, when the next digit is drawn, it could balance an
# unbalanced digit (X possibilities), unbalance a digit (5-X+Y
# possibilities), or introduce a previously unseen odd digit
# (5-Y possibilities). This info leads to a transition matrix,
# which can be repeatedly multiplied by itself to get higher Q's.
#
# The null state transitions to itself (1 possibility), X=1,Y=0
# (4 possibilities, since leading zeroes are not allowed) or X=0,Y=1
# (5 possibilities).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matrixmult

def solve():
    start = time()
    mod = 1000000123
    matrix = [[0 for col in range(52)] for row in range(52)]
    balanced_indices = [1, 7, 14, 22, 31, 41]   # Indices where X=0
    # Set null state transitions
    matrix[0][0] = 1    # Leading zero
    matrix[0][2] = 4    # Start with 2, 4, 6, 8 (unbalancing)
    matrix[0][7] = 5    # Start with 1, 3, 5, 7, 9
    # Set other transitions
    for y in range(6):
        for x in range(y + 6):
            index = balanced_indices[y] + x
            if x != 0:  # If at least one digit is unbalanced
                matrix[index][index - 1] = x
            if x != y + 5:  # If at least one digit is balanced
                matrix[index][index + 1] = 5 - x + y
            if y != 5:  # If at least one odd digit has not appeared
                matrix[index][index + 6 + y] = 5 - y
    result = 0    
    for twopow in range(1, 40):
        matrix = matrixmult(matrix, matrix, mod)
        # 0-digit number in null state, so count balanced states in top row
        for balanced_index in balanced_indices:
            result += matrix[0][balanced_index]
        result %= mod
    peresult(520, result, time() - start)

if __name__ == "__main__":
    solve()
