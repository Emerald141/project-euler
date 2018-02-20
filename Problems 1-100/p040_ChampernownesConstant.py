# An irrational decimal fraction is created by concatenating
# the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the
# value of the following expression.
#
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

# THEORY:
#
# The 1-digit numbers take up 9 * 1 = 9 decimal places.
# The 2-digit numbers take up 90 * 2 = 180 decimal places.
# The 3-digit numbers take up 900 * 3 = 2700 decimal places.
# etc.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    result = 1
    for exp in range(7):
        place = 10 ** exp
        digits_per_int = 1
        while place > 10 ** (digits_per_int - 1) * 9 * digits_per_int:
            # Skip over all the k-digit integers
            place -= 10 ** (digits_per_int - 1) * 9 * digits_per_int
            digits_per_int += 1
        # Find the integer that the digit lies inside, and place within that int
        target_num = 10 ** (digits_per_int - 1) + (place - 1) // digits_per_int
        small_place = (place - 1) % digits_per_int
        result *= int(str(target_num)[small_place])
    return result

if __name__ == "__main__":
    start = time()
    peresult(40, solve(), time() - start)
