# Let's call two numbers friend numbers if their representation in base 10 has
# at least one common digit.
# E.g. 1123 and 3981 are friend numbers.
#
# Let f(n) be the number of pairs (p,q) with 1≤p<q<n such that p and q are
# friend numbers.
# f(100)=1539.
#
# Find f(10^18) mod 1000267129.

# THEORY:
#
# It's easier to find the number of unfriendly pairs first, then subtract that
# from the total number of pairs to get the number of friendly pairs.
#
# Initially, consider (p, q) and (q, p) distinct pairs; we'll divide by 2
# at the end.
#
# We can start by counting the integers with, and only with, a 1 in their
# digits, and multiplying them by the count of numbers only with (but not
# necessarily with) a 2,3,4,5,6,7,8,9,0 in their digits. Then we can repeat with
# 2 and 1,3,4,5,6,7,8,9,0. There are (9 choose 1) such cases.
#
# Next consider the integers with and only with a 0 and 1 in their digits.
# Multiply with the count of numbers only with 2,3,4,5,6,7,8,9.
# Repeat with 0,2 and 1,3,4,5,6,7,8,9. There are (9 choose 1) such cases.
# (We need to consider 0 separately from the other digits because it's
# something of a special case; integers can't have leading 0's.)
#
# There are (9 choose 2) cases analogous to 1,2 and 3,4,5,6,7,8,9,0.
# There are (9 choose 2) cases analogous to 0,1,2 and 3,4,5,6,7,8,9.
# There are (9 choose 3) cases analogous to 1,2,3 and 4,5,6,7,8,9,0.
# There are (9 choose 3) cases analogous to 0,1,2,3 and 4,5,6,7,8,9.
# etc.
# There are (9 choose 8) cases analogous to 1,2,3,4,5,6,7,8 and 9,0.
# There are (9 choose 8) cases analogous to 0,1,2,3,4,5,6,7,8 and 9.
#
# Add all these up, divide by 2, and subtract from the total number of pairs,
# which is (n-1)(n-2)/2.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import choose

def count_with_and_only_with(total_digit_count, digit_count, has_zero):
    # num_counts[i] = count of numbers that have i distinct digits
    # (drawn from the digit pool)
    num_counts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = 0
    for next_digit in range(total_digit_count):
        new_num_counts = [0 for i in range(10)]
        for i in range(10):
            new_num_counts[i] += i * num_counts[i]
            if i < 9:
                new_num_counts[i+1] += (digit_count - i) * num_counts[i]
        result += new_num_counts[digit_count]
        num_counts = new_num_counts
    if has_zero:
        # (1 / digit_count) of these numbers began with a zero
        result //= digit_count
        result *= digit_count - 1
    return result

def count_only_with(total_digit_count, digit_count, has_zero):
    result = 0
    for exponent in range(1, total_digit_count + 1):
        result += digit_count ** exponent
    if has_zero:
        # (1 / digit_count) of these numbers began with a zero
        result //= digit_count
        result *= digit_count - 1
    return result

def solve(total_digit_count = 18, mod = 1000267129):
    cap = 10 ** total_digit_count
    # Result is initially the total number of pairs, counting duplicates.
    # Non-friends will be subtracted.
    # Modulo is multiplied by 2 so that duplicates can be removed later.
    result = (cap - 1) * (cap - 2) % (2 * mod)
    for digit_count in range(1, 9):
        result -= choose(9, digit_count) \
         * count_with_and_only_with(total_digit_count, digit_count, False) \
         * count_only_with(total_digit_count, 10 - digit_count, True)
        result -= choose(9, digit_count) \
         * count_with_and_only_with(total_digit_count, digit_count + 1, True) \
         * count_only_with(total_digit_count, 9 - digit_count, False)
        result %= 2 * mod
    result //= 2
    return result

if __name__ == "__main__":
    start = time()
    peresult(612, solve(18), time() - start)
