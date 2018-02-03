# The Fibonacci sequence is defined by the recurrence relation:
#
# F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
# Hence the first 12 terms will be:
#
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
# F(10) = 55
# F(11) = 89
# F(12) = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence
# to contain 1000 digits?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(digit_count = 1000):
    previous = 1
    current = 1
    index = 2
    while current < 10 ** (digit_count - 1):
        index += 1
        previous, current = current, previous + current
    return index

if __name__ == "__main__":
    start = time()
    peresult(25, solve(), time() - start)
