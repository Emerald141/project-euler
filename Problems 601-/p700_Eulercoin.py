# Leonhard Euler was born on 15 April 1707.
#
# Consider the sequence 1504170715041707n mod 4503599627370517.
#
# An element of this sequence is defined to be an Eulercoin if it is strictly
# smaller than all previously found Eulercoins.
#
# For example, the first term is 1504170715041707 which is the first Eulercoin.
# The second term is 3008341430083414 which is greater than 1504170715041707
# so is not an Eulercoin. However, the third term is 8912517754604 which is
# small enough to be a new Eulercoin.
#
# The sum of the first 2 Eulercoins is therefore 1513083232796311.
#
# Find the sum of all Eulercoins.

# THEORY:
#
# This is kind of cheating, but I counted the first few Eulercoins, and they
# start to slow down after the coin 15806432.
# After that, just multiply each i in ascending order by the inverse of
# 1504170715041707, and record the resulting n.
# If it's greater than any preceding n, then i isn't an Eulercoin. Else, it is.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    cutoff = 15806432
    # Part 1: Count all coins greater than and including the cutoff
    a = 1504170715041707
    mod = 4503599627370517
    coin = mod  # Upper bound
    total = 0
    term = 0
    while coin != cutoff:
        term = (term + a) % mod
        if term < coin:
            coin = term
            total += coin
    # Part 2: Count all coins preceding the cutoff
    coin_n = mod  # Upper bound
    a_inv = pow(a, mod - 2, mod)
    for i in range(1, cutoff):
        n = (i * a_inv) % mod
        if n < coin_n:
            coin_n = n
            total += i
    return total

if __name__ == "__main__":
    start = time()
    peresult(700, solve(), time() - start)
