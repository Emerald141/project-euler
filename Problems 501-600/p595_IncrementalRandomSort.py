# A deck of cards numbered from 1 to n is shuffled randomly such that each
# permutation is equally likely.
#
# The cards are to be sorted into ascending order using the following technique:
#
# 1. Look at the initial sequence of cards. If it is already sorted, then there
# is no need for further action. Otherwise, if any subsequences of cards happen
# to be in the correct place relative to one another (ascending with no gaps),
# then those subsequences are fixed by attaching the cards together. For
# example, with 7 cards initially in the order 4123756, the cards labelled 1, 2
# and 3 would be attached together, as would 5 and 6.
#
# 2. The cards are 'shuffled' by being thrown into the air, but note that any
# correctly sequenced cards remain attached, so their orders are maintained.
# The cards (or bundles of attached cards) are then picked up randomly. You
# should assume that this randomisation is unbiased, despite the fact that some
# cards are single, and others are grouped together.
#
# 3. Repeat steps 1 and 2 until the cards are sorted.
#
# Let S(n) be the expected number of shuffles needed to sort the cards. Since
# the order is checked before the first shuffle, S(1) = 0. You are given that
# S(2) = 1, and S(5) = 4213/871.
#
# Find S(52), and give your answer rounded to 8 decimal places.

# THEORY:
#
# Let A(n, k) be the number of ways to sort n cards such that there are k
# streaks of consecutive ascending cards.
# If k < 1 or k > n, A(n, k) = 0.
# A(1, 1) = 1.
# If A(n, k) is known for all k, then A(n+1, k) can be calculated for all k:
#   Initially set A(n+1, k) to 0 for all k.
#   Iterate over k from 1 to n:
#       Add A(n, k) to A(n+1, k), representing the n'th card being placed
#           directly after the (n-1)th card.
#       Add k * A(n, k) to A(n+1, k+1), representing the n'th card being placed
#           between two streaks of ascending cards.
#       Add (n - k) * A(n, k) to A(n+1, k+2), representing the n'th card being
#           placed in the middle of a streak of ascending cards, breaking it
#           into two streaks (and adding a 1-card streak of the card itself).
#
# Let E(n) be the expected number of shuffles to sort n cards, if we shuffle
# BEFORE we check the order of the cards (unless there's only one card).
# Then E(n) = 1 + (sum of k=1 to n) A(n, k) / n! * E(k)
# except for E(1), which is equal to 0.
# This is because staping n cards together into k piles is essentially the same
# as whittling down the deck to k cards.
#
# S(n) = E(n) - 1, because the game starts with a "free" shuffle.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matsolve

def solve(card_count = 52):
    if card_count < 2:
        return 0
    # a[n][k] = A(n + 1, k + 1)
    a = [ [0 for k in range(card_count + 1)] for n in range(card_count)]
    a[0][0] = 1
    for n in range(card_count - 1):
        for k in range(n + 1):
            a[n+1][k] += a[n][k]
            a[n+1][k+1] += a[n][k] * (k + 1)
            if k < n:
                a[n+1][k+2] += a[n][k] * (n - k)
    # the matrix "a" now gets repurposed to calculate "e"
    factorial = 1
    for n in range(1, card_count):
        factorial *= n + 1
        a[n][n] -= factorial
        a[n][card_count] = -factorial
    matsolve(a)
    return "{:.8f}".format(a[-1][-1] - 1)

if __name__ == "__main__":
    start = time()
    peresult(595, solve(), time() - start)
