# Anton and Bertrand love to play three pile Nim.
# However, after a lot of games of Nim they got bored and changed the rules
# somewhat.
# They may only take a number of stones from a pile that is a proper divisor
# of the number of stones present in the pile.
# E.g. if a pile at a certain moment contains 24 stones they may take only
# 1,2,3,4,6,8 or 12 stones from that pile.
# So if a pile contains one stone they can't take the last stone from it as
# 1 isn't a proper divisor of 1.
# The first player that can't make a valid move loses the game.
# Of course both Anton and Bertrand play optimally.
#
# The triple (a,b,c) indicates the number of stones in the three piles.
# Let S(n) be the number of winning positions for the next player for
# 1 ≤ a, b, c ≤ n.
# S(10) = 692 and S(100) = 735494.
#
# Find S(123456787654321) modulo 1234567890.

# THEORY:
#
# As per the Sprague-Grundy theorem, every pile is equivalent to a nimber, and
# the nimber of all piles is equivalent to the XOR of their individual nimbers.
# The nimber of a pile is the smallest non-negative number which isn't the
# nimber of a pile which can be reached from it.
#
# Let f(n) denote the nimber of a pile of size n.
# By induction, f(n) is the exponent of the largest power of 2 which divides n.
# This is true in the base case where n = 1; no stones can be taken so the
# nimber is 0.
#
# In the inductive case, there exist nonnegative m and positive odd r
# such that n = 2^m * r.
# Then for all k < m, 2^k properly divides n, so a pile of n - 2^k stones
# is reachable from a pile of n stones.
# Then n - 2^k = 2^k * (2^(m-k) * r - 1), the right term of which is odd,
# so f(n - 2^k) = k by the inductive hypothesis.
# Therefore f(n) >= m.
#
# Now assume f(n) > m; then there exists a proper divisor d of n such that
# f(n - d) = m. Then there exists positive odd s such that n - d = 2^m * s,
# and thus d = 2^m * (r - s). Because (r - s) is even, 2^(m+1) divides d.
# But 2^(m+1) does not divide n, so d does not divide n, a contradiction.
# Therefore f(n) = m and the proof is complete.
#
# The first player wins if and only if the game's total nimber (i.e. the XOR
# of the nimbers of all three piles) is nonzero.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import row_matrix_pow_mult
from math import log

def solve(cap = 123456787654321, mod = 1234567890):
	# Step 1: For each m, get the count of numbers n for which f(n) >= m
    nimbers = [cap // (2 ** m) for m in range(int(log(cap, 2)) + 1)]
    # Step 2: For each m, get the count of numbers n for which f(n) = m
    for i in range(len(nimbers) - 1):
        nimbers[i] -= nimbers[i+1]
    # Step 3: Find number of positions with zero total nimber (losing positions)
    losing_positions = 0
    for a in range(len(nimbers)):
        for b in range(len(nimbers)):
            if a ^ b < len(nimbers):
                losing_positions += nimbers[a] * nimbers[b] * nimbers[a ^ b]
                losing_positions %= mod
    # Step 4: Subtract losing positions from total positions
    return (pow(cap, 3, mod) - losing_positions) % mod

if __name__ == "__main__":
	start = time()
	peresult(509, solve(), time() - start)
