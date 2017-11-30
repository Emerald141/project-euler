# Nim is a game played with heaps of stones, where two players take it
# in turn to remove any number of stones from any heap until no stones remain.
# 
# We'll consider the three-heap normal-play version of Nim, which works
# as follows:
# - At the start of the game there are three heaps of stones.
# - On his turn the player removes any positive number of stones from any
# single heap.
# - The first player unable to move (because no stones remain) loses.
# 
# If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1,
# n2 and n3 then there is a simple function X(n1,n2,n3) — that you may
# look up or attempt to deduce for yourself — that returns:
# - zero if, with perfect strategy, the player about to move will eventually
# lose; or
# - non-zero if, with perfect strategy, the player about to move will
# eventually win.
# 
# For example X(1,2,3) = 0 because, no matter what the current player does,
# his opponent can respond with a move that leaves two heaps of equal size,
# at which point every move by the current player can be mirrored by his
# opponent until no stones remain; so the current player loses. To illustrate:
# - current player moves to (1,2,1)
# - opponent moves to (1,0,1)
# - current player moves to (0,0,1)
# - opponent moves to (0,0,0), and so wins.
# 
# For how many positive integers n ≤ 2^30 does X(n,2n,3n) = 0 ?

# THEORY:
# The Nim function alluded to in the problem is the checksum of the
# three piles.
# Thus we're looking for all n such that
# n XOR 2n XOR 3n = 0,
# i.e. n XOR 2n = n + 2n.
# This is true if and only if, when we're adding n and 2n, we never
# have to do a bit carry, which is true if and only if there are no
# 1's right next to each other.
#
# If we have x 1's, then the first x-1 of these 1's are immediately followed
# by a 0. We can treat each 1 and its 0 as a single "block"; each independent
# 0 is a "block" by itself.
# This means we have 31-x blocks, x of which are 1's.
# So it's just a matter of taking 31-x choose x, and
# then summing that over all possible x.
# Because n is positive, x >= 1; because there are 30 digits in total,
# n <= 15.
#
# We've also got to add one result for 2^30 itself.
#
# The answer ends up being the 32nd Fibonacci number, a fact I find curious.

from time import time
from peresult import peresult
from probability import choose

def pe301():
    start = time()
    result = 1  # 2^30 itself (all other solutions are 30-bit)
    for x in range(1, 16):
        result += choose(31-x, x)
    peresult(301, result, time() - start)

if __name__ == "__main__":
    pe301()
