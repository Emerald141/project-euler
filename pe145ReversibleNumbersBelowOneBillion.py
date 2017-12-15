# Some positive integers n have the property that the sum [ n + reverse(n) ]
# consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
# 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
# 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (10^9)?

# THEORY:
#
# There are 100 pairs of digits total (10 ^ 2)
# 30 have an odd sum less than 10. Out of these, 20 don't contain a 0.
# 20 have an odd sum and are greater than 10. All of them don't contain a 0.
# 25 have an even sum and are less than 10.
# 25 have an even sum and are greater than or equal to 10.
#
# If n has 2 * k digits for some k, then each of the k pairs of digits must
# have an odd sum less than 10. The pair on the outside additionally cannot
# contain a 0. The number of valid n is therefore 30 ^ (k - 1) * 20.
#
# If n has 4 * k + 3 digits for some k, then from the outside going in,
# the pairs alternate: odd > 10, even < 10, odd > 10, even < 10...
# and so on, until the middle "pair" of two of the same element is less
# than 10. There are 5 possible "combinations" for this "pair": 0, 1, 2, 3, 4.
# The number of valid n is therefore 20 ^ (k + 1) * 25 ^ k * 5
# = 500 ^ k * 100.
#
# If n has 4 * k + 1 digits for some k, n is not reversible.

# I solved this one by hand, but decided to write up the program anyway
# for my own curiosity. 10^9 is a low cap.

from time import time
from peresult import peresult

def pe145(max_digits = 9):
    start = time()
    result = 0
    for digits in range(1, max_digits + 1):
        if digits % 2 == 0:
            result += 30 ** (digits // 2 - 1) * 20
        elif digits % 4 == 3:
            result += 500 ** (digits // 4) * 100
    peresult(145, result, time() - start)

if __name__ == "__main__":
    pe145()
