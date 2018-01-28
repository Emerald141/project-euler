# Let A and B be bit strings (sequences of 0's and 1's).
# If A is equal to the leftmost length(A) bits of B, then A is said to be
# a prefix of B.
# For example, 00110 is a prefix of 001101001, but not of 00111 or 100110.
# 
# A prefix-free code of size n is a collection of n distinct bit strings
# such that no string is a prefix of any other. For example, this is a
# prefix-free code of size 6:
# 
# 0000, 0001, 001, 01, 10, 11
# 
# Now suppose that it costs one penny to transmit a '0' bit, but four pence
# to transmit a '1'.
# Then the total cost of the prefix-free code shown above is 35 pence, which
# happens to be the cheapest possible for the skewed pricing scheme in question.
# In short, we write Cost(6) = 35.
# 
# What is Cost(10^9)?

# THEORY:
# 
# The lowest-cost prefix-free code of size n, A(n), is created by taking a
# least-expensive element of A(n-1), duplicating it, and appending a 0 to
# one of the duplicates and a 1 to the other. Thus if the least-expensive
# element of A(n-1) costs x pence, Cost(n) = Cost(n-1) + x + 5.
# 
# As a consequence of the above algorithm, there are at most five unique
# costs in any A(n): x, x+1, x+2, x+3, and x+4.
#
# Let f(x) be the maximum number of strings with cost x in any A(n).
# f(x) = 0 for x < 0.
# f(0) = 1.
# f(x) = f(x-1) + f(x-4) in general.
#
# For any x, there exists n such that A(n) is composed of f(x) strings of
# cost x, f(x-3) strings of cost x+1, f(x-2) strings of cost x+2, and
# f(x-1) strings of cost x+3.
#
# Find the largest such n below 10^9, and its corresponding x.
# Let d = 10^9 - n be the number of strings that must be added to A(n).
# Then d of the strings with cost x must be added, so
# Cost(10^9) = x*f(x) + (x+1)*f(x-3) + (x+2)*f(x-2) + (x+3)*f(x-3) + d(x+5).

from time import time
from peresult import peresult

def pe219(cap = 10 ** 9):
    start = time()
    x = -1
    f = [0, 0, 0, 0, 1]
    while f[4] + f[1] + f[2] + f[3] < cap:
        x += 1
        f = f[1:] + [f[1] + f[4]]
    d = cap - f[0] - f[1] - f[2] - f[3]
    result = x * f[3] + (x+1) * f[0] + (x+2) * f[1] + (x+3) * f[2] + d * (x+5)
    peresult(219, result, time() - start)

if __name__ == "__main__":
    pe219()
