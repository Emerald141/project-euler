# For non-negative integers m, n, the Ackermann function A(m,n)
# is defined as follows:
# A(m,n) = n + 1              if m = 0
# A(m,n) = A(m−1,1)           if m > 0 and n = 0
# A(m,n) = A(m−1,A(m,n−1))    if m > 0 and n > 0
# For example A(1,0)=2, A(2,2)=7 and A(3,4)=125.
#
# Find A(0,0) + A(1,1) + A(2,2) + ... + A(6,6) and give your answer mod 14^8.

# THEORY:
#
# This is an exercise in hyperoperations.
# A(0,n) = n + 1
# A(1,n) = 2 + (n + 3) - 3
# A(2,n) = 2 * (n + 3) - 3
# A(3,n) = 2 ^ (n + 3) - 3
# A(4,n) = 2 ↑↑ (n + 3) - 3
# A(5,n) = 2 ↑↑↑ (n + 3) - 3
# A(6,n) = 2 ↑↑↑↑ (n + 3) - 3
#
# Copied from the theory for problem 188:
# For coprime M and x, x^phi(M) mod M = 1, where phi is Euler's totient.
# Then x^phi(phi(M)) mod phi(M) = 1.
# Using these two facts in combination yields x^x^phi(phi(M)) mod M = 1.
# So x^x^x^phi(phi(phi(M))) mod M = 1, and so on.
#
# At each stage of the tetration, one only has to take the result modulo
# phi(phi(...(phi(M))...)).
# For all but a few, that modulus is 1, so those steps can be skipped.
# The power towers for m=5 and m=6 are long enough that their moduli
# will be the same.
#
# If Y is the power tower modulo 7^8, and we know it's zero modulo 2^8,
# then if Z is the inverse of 2^8 modulo 7^8, the power tower is equivalent
# to Y * 2^8 * Z modulo 14^8.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def phi237(n):
    # Return the totient of a number whose sole prime factors are 2, 5, and 7.
    if n % 2 == 0: n //= 2
    if n % 3 == 0: n = (n * 2) // 3
    if n % 7 == 0: n = (n * 6) // 7
    return n

def solve():
    # A(0,0) + A(1,1) + A(2,2) + A(3,3)
    result = sum([0 + 1, 2 + (1 + 3) - 3, 2 * (2 + 3) - 3, 2 ** (3 + 3) - 3])
    # Preparation for remaining steps
    mods = [7 ** 8]
    while mods[-1] != 1:
        mods.append(phi237(mods[-1]))
    # inverse of x modulo M (coprime) is x^(phi(M) - 1)
    inv = pow(2 ** 8, phi237(7 ** 8) - 1, 7 ** 8)
    # A(4,4)
    term = 2
    for mod in mods[(4+3)-2::-1]:
        term = pow(2, term, mod)
    term = (2 ** 8 * term * inv) % 14 ** 8
    result += term - 3
    # A(5,5) and A(6,6)
    term = 0
    for mod in mods[::-1]:
        term = pow(2, term, mod)
    term = (2 ** 8 * term * inv) % 14 ** 8
    result += 2 * (term - 3)
    return result % (14 ** 8)

if __name__ == "__main__":
    start = time()
    peresult(282, solve(), time() - start)
