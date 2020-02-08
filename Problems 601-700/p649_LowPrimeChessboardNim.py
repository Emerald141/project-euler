# Alice and Bob are taking turns playing a game consisting of c different
# coins on a chessboard of size n by n.
# The game may start with any arrangement of c coins in squares on the board.
# It is possible at any time for more than one coin to occupy the same square
# on the board at the same time. The coins are distinguishable, so swapping
# two coins gives a different arrangement if (and only if) they are on
# different squares.
#
# On a given turn, the player must choose a coin and move it either left or up
# 2, 3, 5, or 7 spaces in a single direction. The only restriction is that the
# coin cannot move off the edge of the board.
#
# The game ends when a player is unable to make a valid move, thereby granting
# the other player the victory.
#
# Assuming that Alice goes first and that both players are playing optimally,
# let M(n,c) be the number of possible starting arrangements for which Alice
# can ensure her victory, given a board of size n by n with c distinct coins.
#
# For example, M(3,1)=4, M(3,2)=40, and M(9,3)=450304.
#
# What are the last 9 digits of M(10000019,100)?

# THEORY:
#
# The coins don't interact, and vertical and horizontal motion are independent.
# So the problem is equivalent to a game of Nim with 2c piles, each of which
# contains between 0 and n-1 stones. Players can remove 2, 3, 5, or 7 stones
# from a single pile on their turn, and the last player to take a stone wins.
#
# Consider four "tiers" of stone counts, modulo 9.
# Tier 0: 0 and 1
# Tier 1: 2 and 3
# Tier 2: 4 and 5
# Tier 3: 6 and 7
# Tier 4: 8
#
# Any action performed on a pile of stones affects its tier. Any higher tier can
# always transition to any lower tier. A lower tier can sometimes transition to
# a higher tier, but the next player can immediately undo this action, so for
# practical purposes, tiers can only go down.
#
# When a pile of stones is in Tier 0, either player can force there to be an
# even number of actions remaining to be performed on the pile. Thus, when all
# piles are in Tier 0, the next player to move will lose. The winner will
# therefore be the player who moves the last pile into Tier 0.
#
# The problem is therefore reducible to a game of "meta-Nim" with 2c piles of
# between 0 and 4 "meta-stones" determined by the tier of the real pile.
# The losing positions for the first player are those where the Nim function is
# 0 on these meta-piles: that is, there are an even number of piles in tier 4,
# and the parity of the number of piles in tiers 1, 2, and 3 is equivalent.
#
# Conveniently enough, 10000019 is equivalent to 2 mod 9, so there are an equal
# number of possible numbers in tiers 1, 2, and 3.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from probability import choose

def solve(n = 10000019, c = 100, mod = 10 ** 9):
    cap = 2 * c
    if n % 9 > 2:
        print("Error: Unequal number of possible values in tiers 1, 2, and 3")
        return -1
    low_choices = 2 * (n // 9) + (n % 9)
    mid_choices = 2 * (n // 9)
    high_choices = n // 9

    low_mults = [ pow(low_choices, x, mod) % mod for x in range(cap + 1)]
    mid_mults = [ [ (choose(y, x) * pow(mid_choices, x, mod)) % mod         \
      for x in range(y + 1)] for y in range(cap + 1)]
    high_mults = [ (choose(cap, x) * pow(high_choices, x, mod)) % mod       \
      for x in range(cap + 1)]

    losing_positions = 0
    for h in range(0, cap + 1, 2):
        for m1 in range(0, cap - h + 1):
            for m2 in range(m1 % 2, m1 + 1, 2):
                for m3 in range(m1 % 2, min(m2 + 1, cap - h - m1 - m2 + 1), 2):
                    term = high_mults[h]
                    remaining = cap - h
                    for m in [m1, m2, m3]:
                        term *= mid_mults[remaining][m]
                        remaining -= m
                    term *= low_mults[remaining]
                    if len(set([m1, m2, m3])) == 3:\
                        term *= 6
                    elif len(set([m1, m2, m3])) == 2:
                        term *= 3
                    losing_positions += term
                    losing_positions %= mod
    return (pow(n, cap, mod) - losing_positions) % mod

if __name__ == "__main__":
    start = time()
    peresult(649, solve(), time() - start)
