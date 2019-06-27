# A hexagonal orchard of order n is a triangular lattice made up of points
# within a regular hexagon with side n. The following is an example of a
# hexagonal orchard of order 5:
# 
#      X O O O O X
#     O X O X O X O
#    O O X O O X O O
#   O X O X O X O X O
#  O O O O O O O O O O
# X X X X O O O X X X X
#  O O O O O O O O O O
#   O X O X O X O X O
#    O O X O O X O O
#     O X O X O X O
#      X O O O O X
# 
# The X's are the points which are hidden from the center by a point closer to 
# it. It can be seen that for a hexagonal orchard of order 5, 30 points are 
# hidden from the center.
# 
# Let H(n) be the number of points hidden from the center in a hexagonal
# orchard of order n.
# 
# H(5) = 30. H(10) = 138. H(1 000) = 1177848.
# 
# Find H(100 000 000).

# THEORY:
# 
# The orchard has 6-rotational symmetry, so we can focus on a single triangle
# and multiply the number of hidden points by 6 to get the result.
# Consider the top triangle of order 6, skewed for ease of analysis:
# 
# | O X X X O X
# | O O O O X
# | O X O X
# | O O X
# | O X
# | O
# C - - - - - -
# 
# C is the center of the hexagon.
# If the point (a,b) in this triangle is blocked by some closer point (c,d),
# then (a,b), (c,d), and (0,0) form a line.
# This implies that (a,b) = k(c,d) for some k>1, so a and b are not coprime.
# If, however, a and b ARE coprime, then no such line exists and (a,b) is
# not hidden from the center.
# The number of unhidden points in the triangle is therefore equal to the size
# of the set { (a,b) : 1 <= a <= b <= n, gcd(a,b) = 1}.
# This is equal to P(n), the sum of phi(i) for i between 1 and n.
# The number of hidden points in the triangle is equal to n(n+1)/2 minus this.

# To calculate P(n) for large n, consider the functions:
#   F(n)   = | { (a,b) : 1 <= a <= b <= n } | = n(n+1)/2
#   R_i(n) = | { (a,b) : 1 <= a <= b <= n, gcd(a,b) = i } |
# Note that P(n) = R_1(n).
# Note also that if gcd(a,b) = 1, then gcd(ka, kb) = k.
# This implies that R_i(n) = P(n/i) for all i.
# Therefore
#   P(n) = F(n) - [R_2(n) + R_3(n) + ... + R_n(n)]
#        = n(n+1)/2 - [P(n/2) + P(n/3) + ... + P(n/n)].

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def get_p(n, memos):
	if n in memos:
		return memos[n]
	result = n * (n + 1) // 2
	denom = 2
	while denom <= n:
		arg = n // denom
		new_denom = n // arg + 1
		result -= get_p(arg, memos) * (new_denom - denom)
		denom = new_denom
	memos[n] = result
	return result	

def solve(cap = 10 ** 8):
	return 6 * (cap * (cap + 1) // 2 - get_p(cap, {1: 1}))

if __name__ == "__main__":
	start = time()
	peresult(512, solve(), time() - start)
