# The hyperexponentiation or tetration of a number a by a positive integer b,
# denoted by a↑↑b, is recursively defined by:
#
# a↑↑1 = a,
# a↑↑(k+1) = a(a↑↑k).
#
# Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987
# and 3↑↑4 is roughly 10^(3.6383346400240996*10^12).
#
# Find the last 8 digits of 1777↑↑1855.

# THEORY:
#
# For any M and x, x^phi(M) mod M = 1, where phi is Euler's totient function.
# Then x^phi(phi(M)) mod phi(M) = 1.
# Using these two facts in combination yields x^x^phi(phi(M)) mod M = 1.
# So x^x^x^phi(phi(phi(M))) mod M = 1, and so on.
#
# At each stage of the tetration, one only has to take the result modulo
# phi(phi(...(phi(M))...)).
# For all but a few, that modulus is 1, so those steps can be skipped.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    mods = [10 ** 8]
    while mods[-1] != 1:
        # phi(10^k) = 4 * 10^(k-1)
        # phi(2^k) = 2^(k-1)
        if mods[-1] % 5 == 0:
            mods.append(mods[-1] * 2 // 5)
        else:
            mods.append(mods[-1] // 2)
    result = 0
    for mod in mods[::-1]:
        result = pow(1777, result, mod)
    return result

if __name__ == "__main__":
    start = time()
    peresult(188, solve(), time() - start)
