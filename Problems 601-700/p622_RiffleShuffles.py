# A riffle shuffle is executed as follows: a deck of cards is split into two
# equal halves, with the top half taken in the left hand and the bottom half
# taken in the right hand. Next, the cards are interleaved exactly, with the
# top card in the right half inserted just after the top card in the left half,
# the 2nd card in the right half just after the 2nd card in the left half, etc.
# (Note that this process preserves the location of the top and bottom card of
# the deck)
#
# Let s(n) be the minimum number of consecutive riffle shuffles needed to
# restore a deck of size n to its original configuration, where n is a
# positive even number.
#
# Amazingly, a standard deck of 52 cards will first return to its original
# configuration after only 8 perfect shuffles, so s(52)=8. It can be verified
# that a deck of 86 cards will also return to its original configuration after
# exactly 8 shuffles, and the sum of all values of n that satisfy s(n)=8 is 412.
#
# Find the sum of all values of n that satisfy s(n)=60.

# THEORY:
#
# The top and bottom cards will never move, so we can forget about them.
# Number all the other cards from 1 to n-2. Then in a riffle shuffle:
#    1 -> 2                (n/2) -> 1
#    2 -> 4                (n/2) + 1 -> 3
#    3 -> 6                (n/2) + 2 -> 5
#    ...                   ...
#    (n/2)-1 -> n-2        n-2 -> n-3
# It can be seen that the k-th card will become the (2k mod (n-1))th card.
# Riffle shuffling N times means that the position of the k-th card gets
# multiplied by 2^N mod (n-1).
# Therefore N riffle shuffles hold the deck in place if and only if 2^N = 1
# mod n-1;
# that is, if n-1 divides 2^N - 1.
#
# Thus we have to sum all n such that n-1 divides 2^60 - 1,
# and such that n-1 divides no smaller 2^m - 1.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(s = 60):
    big = (2 ** s) - 1

    # Step 1: Factor big
    all_primes = primesbelow(1400)  # No larger primes divide 2^60-1
    primes, exp_cap = [], []
    for p in all_primes:
        if big % p == 0:
            primes.append(p)
            exp = 1
            while (big // (p ** exp)) % p == 0:
                exp += 1
            exp_cap.append(exp)

    # Step 2: Find all 2^m-1 smaller than big
    cant_divide = []
    for two_exp in range(2, s):
        cant_divide.append((2 ** two_exp) - 1)

    # Step 3: Iterate among all factors of big.
    # If they don't divide any other 2^m-1, add one plus them to the answer
    factor = 1
    exp = [0 for p in primes]
    result = 0
    while True:
        # Find the next factor of big
        index = 0
        while index < len(primes) and exp[index] == exp_cap[index]:
            factor //= primes[index] ** exp[index]
            exp[index] = 0
            index += 1
        if index == len(primes):
            return result
        factor *= primes[index]
        exp[index] += 1
        # We have a factor; time to see if it works
        for bad in cant_divide:
            if bad % factor == 0:
                break
        else:
            result += factor + 1

if __name__ == "__main__":
    start = time()
    peresult(622, solve(), time() - start)
