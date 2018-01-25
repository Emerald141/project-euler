# Let n be a positive integer.
# A 6-sided die is thrown n times. Let c be the number of pairs of
# consecutive throws that give the same value.
#
# For example, if n = 7 and the values of the die throws are (1,1,5,6,6,6,3),
# then the following pairs of consecutive throws give the same value:
# ((1,1),5,6,6,6,3)
# (1,1,5,(6,6),6,3)
# (1,1,5,6,(6,6),3)
# Therefore, c = 3 for (1,1,5,6,6,6,3).
#
# Define C(n) as the number of outcomes of throwing a 6-sided die n times
# such that c does not exceed π(n).
# For example, C(3) = 216, C(4) = 1290, C(11) = 361912500
# and C(24) = 4727547363281250000.
#
# Define S(L) as ∑ C(n) for 1 ≤ n ≤ L.
# For example, S(50) mod 1 000 000 007 = 832833871.
#
# Find S(50 000 000) mod 1 000 000 007.

# THEORY:
#
# The first die can be any of six values; it won't be the right member
# of a pair of consecutive throws.
# There are six possibilities for every following die: the value of the
# previous die, which increases c for the sequence, and the five other
# possible values, which do not.
# If there are k same-valued consecutive throws out of a total of n throws,
# then the number of such sequences is therefore
#   D(n, k) = 6 * (n-1 choose k) * (5 ^ (n-k-1)).
# C(n) is the sum of D(n, k) for k between 0 and pi(n), inclusive.
#
# If we know C(n-1) and D(n-1, pi(n-1)), and we know whether n is prime,
# we can compute C(n) and D(n, pi(n)) inductively.
# The n'th row of Pascal's triangle totals twice the row above it;
# with the geometric 5 factor, this increases to 6 times in the below
# equation.
#
# If n is not prime, i.e. pi(n) = pi(n-1):
#   D(n, pi(n)) = D(n-1, pi(n-1)) * (n-1) / (n-k-1) * 5
#   C(n) = 6 * C(n-1) - D(n-1, pi(n-1))
# If n is prime, i.e. pi(n) = pi(n-1) + 1:
#   D(n, pi(n)) = D(n-1, pi(n-1)) * (n-1) / (k+1)
#   C(n) = 6 * C(n-1) - D(n-1, pi(n-1)) + D(n, pi(n))
#
# The initial state is D(1, pi(1)) = 6 and C(1) = 6.

from time import time
from peresult import peresult
from primefns import primesbelow

# Credit for the following two functions (to calculate modular inverses):
# https://stackoverflow.com/questions/4798654
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def pe423(cap = 50000000):
    start = time()
    mod = 1000000007
    primes = primesbelow(cap+1) + [cap + 1] # The append allows computation of
                                            # all S(n) where n is larger than
                                            # all primes below cap
    result = 6
    c = 6
    d = 6
    pi = 0
    for n in range(2, cap + 1):
        if n % 1000000 == 0:
            print(n)
        c = 6 * c - d
        if primes[pi] == n: # n is prime
            d = d * (n-1) * modinv(pi + 1, mod)
            c += d
            pi += 1
        else:               # n is not prime
            d = d * (n-1) * 5 * modinv(n - pi - 1, mod)
        c %= mod
        d %= mod
        result += c
        result %= mod
    peresult(423, result, time() - start)

if __name__ == "__main__":
    pe423()
