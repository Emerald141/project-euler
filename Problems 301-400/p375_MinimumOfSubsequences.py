# Let S(n) be an integer sequence produced with the following pseudo-random
# number generator:
# 
# S(0) = 290797 
# S(n+1) = S(n^2) mod 50515093
# Let A(i, j) be the minimum of the numbers S(i), S(i+1), ... , S(j) for i ≤ j.
# Let M(N) = ΣA(i, j) for 1 ≤ i ≤ j ≤ N.
# We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.
# 
# Find M(2 000 000 000).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 2000000000):
	start = 290797
	mod = 50515093
	def next(k):
		return (k ** 2) % mod
	# Step 1: Determine "a" such that S(a) <= S(k) for all k.
	# Also determine the period "p" of repetition.
	a, min_value = 0, mod
	index, value = 1, next(start)
	while value != min_value:
		if value < min_value:
			a, min_value = index, value
		index += 1
		value = next(value)
	p = index - a
	# Step 2: Determine the number "n" of complete periods which start with
	# S(a), and the number b of values after the final such complete period.	
	n = (cap - (a - 1)) // p
	b = (cap - (a - 1)) % p
	# Step 3: Determine the number of pairs which cross between periods.
	# Each such pair (i, j) will have A(i, j) = S(a).
	pair_count = cap * (cap + 1) // 2     # All pairs
	pair_count -= (a - 1) * a // 2        # Pairs before first period
	pair_count -= n * p * (p + 1) // 2    # Pairs in a period
	pair_count -= b * (b + 1) // 2        # Pairs after last period
	result = pair_count * min_value
	# Step 4: Count pairs inside a single period and after the last period.
	# Keep track of mins with a stack.
	stack = []
	index, value = 1, min_value
	while value != min_value or index == 1:
		# Get rid of all superfluous mins
		i = len(stack) - 1
		while i >= 0 and stack[i][0] > value:
			i -= 1
		stack = stack[:i+1] + [(value, index)]
		# Traverse the relevant mins
		result += stack[0][0] * (n + (index <= b))
		for i in range(len(stack) - 1):
			term = stack[i+1][0] * (stack[i+1][1] - stack[i][1])
			result += term * (n + (index <= b))
		index += 1
		value = next(value)
	# Step 5: Count pairs before the first period in the same manner.
	stack = []
	index, value = 1, next(start)
	while value != min_value:
		# Get rid of all superfluous mins
		i = len(stack) - 1
		while i >= 0 and stack[i][0] > value:
			i -= 1
		stack = stack[:i+1] + [(value, index)]
		# Traverse the relevant mins
		result += stack[0][0] * stack[0][1]
		for i in range(len(stack) - 1):
			result += stack[i+1][0] * (stack[i+1][1] - stack[i][1])
		index += 1
		value = next(value)
	return result

if __name__ == "__main__":
	start = time()
	peresult(375, solve(), time() - start)
