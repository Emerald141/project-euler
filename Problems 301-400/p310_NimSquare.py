# Alice and Bob play the game Nim Square.
# Nim Square is just like ordinary three-heap normal play Nim, but the players
# may only remove a square number of stones from a heap.
# The number of stones in the three heaps is represented by the ordered
# triple (a,b,c).
# If 0≤a≤b≤c≤29 then the number of losing positions for the next player is 1160.
# 
# Find the number of losing positions for the next player if 0≤a≤b≤c≤100 000.

# THEORY:
# 
# Every pile of stones in Nim Square corresponds to a nimber.
# This nimber is the smallest nonnegative integer that CAN'T be reached by
# taking some stones away from it.
# The nimber of the entire position is the XOR of the three piles' nimbers.
# It's a losing position if and only if the nimber is 0.
# In a losing position, two piles have the same nimber if and only if the
# third pile has nimber 0.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import count

def solve(cap = 10 ** 5):
	nimbers = [0 for x in range(cap + 1)]
	for x in range(1, cap + 1):
		reachable_nums = []
		for y in count(1):
			if y ** 2 > x:
				break
			reachable_nums.append(nimbers[x - y ** 2])
		for z in count(0):
			if z not in reachable_nums:
				nimbers[x] = z
				break
	counts = [0 for i in range(max(nimbers) + 1)]
	for i in nimbers:
		counts[i] += 1
	result = 0
	for a in range(len(counts)):
		for b in range(len(counts)):
			c = a ^ b
			if c < len(counts):
				result += counts[a] * counts[b] * counts[c]
		result += 3 * counts[a] * counts[0]
	result += 2 * counts[0]
	result //= 6
	return result		

if __name__ == "__main__":
	start = time()
	peresult(310, solve(), time() - start)
