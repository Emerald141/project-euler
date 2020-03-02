# We can easily verify that none of the entries in the first seven rows of
# Pascal's triangle are divisible by 7:
#
#  	 	 	 	 	 	 1
#  	 	 	 	 	 1	 	 1
#  	 	 	 	 1	 	 2	 	 1
#  	 	 	 1	 	 3	 	 3	 	 1
#  	 	 1	 	 4	 	 6	 	 4	 	 1
#  	 1	 	 5	 	10	 	10	 	 5	 	 1
# 1	 	 6	 	15	 	20	 	15	 	 6	 	 1
# However, if we check the first one hundred rows, we will find that only
# 2361 of the 5050 entries are not divisible by 7.
#
# Find the number of entries which are not divisible by 7 in the first one
# billion (10^9) rows of Pascal's triangle.

# THEORY:
#
# If p is prime, then p divides (n choose k) if and only if  there is a carry
# when the subtraction n-k is performed in base p.
#
# For a 7-digit in n, if that digit is t then the corresponding digit of k
# can be 0,1,2,...t.
# Thus if the base 7 representation of n is abcdefg,
# there are (a+1)(b+1)...(g+1) k's for which 7 does not divide (n choose k).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(n = 10 ** 9):
    digits = []
    while n > 0:
        digits.append(n % 7)
        n //= 7
    result = 0
    multiplier = 1
    for i in range(len(digits) - 1, -1, -1):
        result += multiplier * [0, 1, 3, 6, 10, 15, 21][digits[i]] * 28 ** i
        multiplier *= digits[i] + 1
    return result

if __name__ == "__main__":
    start = time()
    peresult(148, solve(), time() - start)
