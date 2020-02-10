# Bob is very familiar with the famous mathematical puzzle/game,
# "Tower of Hanoi," which consists of three upright rods and disks
# of different sizes that can slide onto any of the rods. The game
# begins with a stack of n disks placed on the leftmost rod in descending
# order by size. The objective of the game is to move all of the disks
# from the leftmost rod to the rightmost rod, given the following restrictions:
#
# Only one disk can be moved at a time.
# A valid move consists of taking the top disk from one stack and placing it
# onto another stack (or an empty rod).
# No disk can be placed on top of a smaller disk.
# Moving on to a variant of this game, consider a long room k units
# (square tiles) wide, labeled from 1 to k in ascending order. Three rods
# are placed at squares a, b, and c, and a stack of n disks is placed on the
# rod at square a.
#
# Bob begins the game standing at square b. His objective is to play the
# Tower of Hanoi game by moving all of the disks to the rod at square c.
# However, Bob can only pick up or set down a disk if he is on the same
# square as the rod / stack in question.
#
# Unfortunately, Bob is also drunk. On a given move, Bob will either stumble
# one square to the left or one square to the right with equal probability,
# unless Bob is at either end of the room, in which case he can only move
# in one direction. Despite Bob's inebriated state, he is still capable of
# following the rules of the game itself, as well as choosing when to pick
# up or put down a disk.
#
# Let E(n,k,a,b,c) be the expected number of squares that Bob travels
# during a single optimally-played game. A game is played optimally if
# the number of disk-pickups is minimized.
#
# Interestingly enough, the result is always an integer. For example,
# E(2,5,1,3,5) = 60 and E(3,20,4,9,17) = 2358.
#
# Find the last nine digits of ∑1≤n≤10000 E(n,10^n,3^n,6^n,9^n).

# THEORY:
#
# I've done some inductive analysis, not reproduced in these comments,
#  on the number of times each subpath
# (a to b, a to c, b to a, b to c, c to a, c to b) is traveled.
# The table, for the first few n, is as follows:
#
# n     ab  ac  ba  bc  ca  cb
# 1      0   1   1   0   0   0
# 2      1   1   2   1   0   1
# 3      2   3   3   2   2   2
# 4      5   5   6   5   4   5
# 5     10  11  11  10  10  10
#
# To get the "base" number of times each path is traveled, double the
# previous number, and then add 1 if n is even.
# Then if n is even, add 1 to "ba" and subtract 1 from "ca";
# and if n is odd, add 1 to "ba" and add 1 to "ac".
#
# If t is the current distance on the strip to a target point, and d is the
# distance between the target point and the end square, the expected number
# of squares traveled until the target is reached is 2dt-t^2.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 10 ** 4, mod = 10 ** 9):
    m = 0
    result = 0
    for n in range(1, cap + 1):
        m = m * 2 + ((n % 2) == 0)
        a = pow(3, n, mod)
        b = pow(6, n, mod)
        c = pow(9, n, mod)
        k = pow(10, n, mod)
        t = [b - a, c - a, b - a, c - b, c - a, c - b]
        d = [b - 1, c - 1, k - a, c - 1, k - a, k - b]
        mult = [m, m, m + 1, m, m, m]
        if n % 2 == 1:
            mult[1] += 1
        else:
            mult[4] -= 1
        for i in range(6):
            result += mult[i] * (2 * t[i] * d[i] - t[i] ** 2)
        result %= mod
    return result

if __name__ == "__main__":
    start = time()
    peresult(497, solve(), time() - start)
