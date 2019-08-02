# Two players are playing a game. There are k piles of stones. When it is his
# turn a player has to choose a pile and replace it by two piles of stones
# under the following two conditions:
# 
#  * Both new piles must have a number of stones more than one and less than
#    the number of stones of the original pile.
#  * The number of stones of each of the new piles must be a divisor of the
#    number of stones of the original pile.
# 
# The first player unable to make a valid move loses. 
# Let f(n,k) be the number of winning positions for the first player,
# assuming perfect play, when the game is played with k piles each having
# between 2 and n stones (inclusively).
# f(10,5)=40085.
# 
# Find f(10^7,10^12).
# Give your answer modulo 987654321.

# THEORY:
# 
# As per the Sprague-Grundy theorem, every pile is equivalent to a nimber, and
# the nimber of two piles is equivalent to the XOR of their individual nimbers.
# The nimber of a pile is the smallest non-negative number which isn't the
# nimber of a pair of piles which can be reached from the pile.
# 
# So, a pile of prime order has nimber 0, since it can't be split.
# A pile with two (not necessarily distinct) prime factors can only be split
# into two piles of prime order, which have a collective nimber of 0 XOR 0 = 0,
# so its nimber is 1.
# A pile with three prime factors can be split into piles with nimbers 0 or 1.
# Because 0 XOR 0 = 1 XOR 1 = 0, and 1 XOR 0 = 0 XOR 1 = 1, this pile has
# nimber 2.
# Inducting further yields:
#  * 4 prime factors -> nimber 4
#  * 5 prime factors -> nimber 7
#  * 6 prime factors -> nimber 8
#  * 7 prime factors -> nimber 11
#  * 8 prime factors -> nimber 13
# etc.
# 
# The first player wins if and only if the game's total nimber (i.e. the XOR
# of the nimbers of all its piles) is nonzero.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import row_matrix_pow_mult

def solve(n = 10 ** 7, k = 10 ** 12, mod = 987654321):
	# Step 1: For each i, get the count of nums <= n with i prime factors
	prime_counts = [0 for x in range(n + 1)]
	options = []  # options[i] = count of nums <= n with i+1 prime factors
	for x in range(2, n + 1):
		if not prime_counts[x]:
			# x is prime
			power = x
			while power <= n:
				for mult in range(power, n + 1, power):
					prime_counts[mult] += 1
				power *= x
		if prime_counts[x] - 1 >= len(options):
			options.append(0)
		options[prime_counts[x] - 1] += 1

	# Step 2: Find all possible nimbers of individial piles
	nimbers = [0]  # nimbers[i] = nimber of a number with i+1 prime factors
	reachable = [False]
	for i in range(1, len(options)):
		for nimber in nimbers:
			reachable[nimber ^ nimbers[-1]] = True
		if sum(reachable) == len(reachable):
			reachable = reachable + [False for r in reachable]
		for r in range(len(reachable)):
			if not reachable[r]:
				nimbers.append(r)
				break
	
	# Step 3: Construct the transition matrix between possible nimbers
	mat = [[0 for x in range(len(reachable))] for y in range(len(reachable))]
	for y in range(len(reachable)):
		for i in range(len(nimbers)):
			mat[y][y ^ nimbers[i]] = options[i]

	# Step 4: Apply this transition matrix k times to an empty pile
	# (representing the successive addition of piles)
	row = [x == 0 for x in range(len(reachable))]
	row = row_matrix_pow_mult(row, mat, k, mod)
	return sum(row[1:]) % mod

if __name__ == "__main__":
	start = time()
	peresult(550, solve(), time() - start)
