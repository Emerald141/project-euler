# For a positive integer n, define f(n) to be the number of non-empty
# substrings of n that are divisible by 3. For example, the string
# "2573" has 10 non-empty substrings, three of which represent numbers
# that are divisible by 3, namely 57, 573 and 3. So f(2573)=3.
#
# If f(n) is divisible by 3 then we say that n is 3-like.
#
# Define F(d) to be how many d digit numbers are 3-like. For example,
# F(2)=30 and F(6)=290898.
#
# Find F(10^5). Give your answer modulo 1000000007.

# THEORY:
#
# Suppose, for a given number, there are:
#   X substrings which are divisible by 3
#   A substrings containing the last digit which are divisible by 3
#   B substrings containing the last digit which are equivalent to 1 mod 3
#   C substrings containing the last digit which are equivalent to 2 mod 3
#
# Represent this number with the tuple (X,A,B,C). Mod all four variables by 3.
#
# If a 0, 3, 6, or 9 is appended to this number, the result will have the
# tuple (X+A+1,A+1,B,C).
# If a 1, 4, or 7 is appended to this number, the result will have the
# tuple (X+C,C,A+1,B).
# If a 2, 5, or 8 is appended to this number, the result will have the
# tuple (X+B,B,C,A+1).
#
# Use dynamic programming. Initially there are three (1,1,0,0) tuples,
# three (0,0,1,0) tuples, and three (0,0,0,1) tuples, because there can be
# no leading zeroes.
# The final result will be the number of tuples where X is 0.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import row_matrix_pow_mult

def index_to_tuple(n):
    return ((n // 27) % 3, (n // 9) % 3, (n // 3) % 3, n % 3)

def tuple_to_index(t):
    return (t[0] % 3) * 27 + (t[1] % 3) * 9 + (t[2] % 3) * 3 + (t[3] % 3)

def solve(power = 10 ** 5, mod = 1000000007):
    mat = [[0 for col in range(81)] for row in range(81)]
    for row in range(81):
        t = index_to_tuple(row)
        mat[row][tuple_to_index((t[0] + t[1] + 1, t[1] + 1, t[2], t[3]))] += 4
        mat[row][tuple_to_index((t[0] + t[3], t[3], t[1] + 1, t[2]))] += 3
        mat[row][tuple_to_index((t[0] + t[2], t[2], t[3], t[1] + 1))] += 3
    input = [0 for x in range(81)]
    input[tuple_to_index((1,1,0,0))] = 3
    input[tuple_to_index((0,0,1,0))] = 3
    input[tuple_to_index((0,0,0,1))] = 3
    output = row_matrix_pow_mult(input, mat, power - 1, mod)
    return sum(output[:27])

if __name__ == "__main__":
    start = time()
    peresult(692, solve(), time() - start)
