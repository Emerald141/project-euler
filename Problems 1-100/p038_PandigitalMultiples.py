# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product
# of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which
# is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can
# be formed as the concatenated product of an integer with
# (1,2, ... , n) where n > 1?

# THEORY:
#
# We're given that 918273645 is a valid pandigital, so the largest valid
# pandigital must start with a 9 in order to be larger.
# This means that the second term (and the third, if it exists) will have one
# more digit than the first term, which starts with a 9.
# The possibilities are thus:
#   9 18 27 36 45   <-- already given
#   9X 1YY ZZZ WWW  <-- overflows the nine-digit limit
#   9XX YYYY ZZZZ   <-- overflows the nine-digit limit
#   9XXX YYYYY      <-- the only remaining possibility
# Therefore if a valid pandigital exists larger than 918273645, it must be
# composed of a four-digit number that starts with 9, prepended to its double.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    for first_num in range(9876, 9123, -1):
        num_string = str(first_num) + str(2 * first_num)
        if len(set(num_string)) == 9 and '0' not in num_string:
            return num_string
    return "918273645"  # if no larger valid pandigital was found

if __name__ == "__main__":
    start = time()
    peresult(38, solve(), time() - start)
