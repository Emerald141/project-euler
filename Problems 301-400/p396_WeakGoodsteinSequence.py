# For any positive integer n, the nth weak Goodstein sequence
# {g1, g2, g3, ...} is defined as:
#
# g1 = n
# for k > 1, gk is obtained by writing gk-1 in base k, interpreting it as a
# base k + 1 number, and subtracting 1.
# The sequence terminates when gk becomes 0.
# For example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}:
#
# g1 = 6.
# g2 = 11 since 6 = 110_2, 110_3 = 12, and 12 - 1 = 11.
# g3 = 17 since 11 = 102_3, 102_4 = 18, and 18 - 1 = 17.
# g4 = 25 since 17 = 101_4, 101_5 = 26, and 26 - 1 = 25.
# and so on.
# It can be shown that every weak Goodstein sequence terminates.
#
# Let G(n) be the number of nonzero elements in the nth weak Goodstein sequence.
# It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381.
# It can also be verified that ΣG(n) = 2517 for 1 ≤ n < 8.
#
# Find the last 9 digits of ΣG(n) for 1 ≤ n < 16.

# THEORY:
#
# For every g, keep track of the base 'x' we're about to convert to, i.e.
# start off with 3 and increment by 1 with every g.
# Keep going until the g becomes 0, then subtract 3.
#
# To decrement 1 from the ones place in g, add 1 to x.
# To decrement 1 from the tens place in g, do the above action x times;
#   this translates to doubling x.
# To decrement 1 from the hundreds place in g, do the above action x times;
#   this translates to multiplying x by 2^x.
# To decrement 1 from the thousands place in g, do the above action x times.
#   First, multiply by 2^x;
#   then, multiply by 2^x raised to itself;
#   then, multiply by THAT raised to itself;
#   and continue this process for x steps.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(mod = 10 ** 9):
    result = 0
    for n in range(1, 16):
        x = 3
        if n % 2 == 1:
            x += 1
        if n % 4 > 1:
            x *= 2
        if n % 8 > 3:
            x *= 2 ** x
        if n % 16 > 7:
            term = 2 ** x
            for i in range(x):  # Thankfully this doesn't break
                x *= term
                x %= mod
                term = pow(term, term, mod)
        result += x - 3
        result %= mod
    return result

if __name__ == "__main__":
    start = time()
    peresult(188, solve(), time() - start)
