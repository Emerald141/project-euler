# Let φ(n) be Euler's totient function.
# 
# Let f(n)=(∑_{i=1}^n φ(n^i)) mod (n+1).
# 
# Let g(n)=∑_{i=1}^n f(i).
# 
# g(100)=2007.
# 
# Find g(5 * 10^8).

# THEORY:
# 
# Note first that the prime factors of n^i are exactly the prime factors of n.
# It follows that φ(n^i) = n^(i-1) * φ(n).
# Then f(n) = φ(n) * (n^(n-1) + n^(n-2) + ... + n + 1) mod (n+1).
# If n is even, then (n+1) divides (n^(n-1) + ... + 1), so f(n) = 0.
# If n is odd, then the remainder when (n^(n-1) + ... + 1) is divided by (n+1)
# is 1, so f(n) = φ(n) mod (n+1).
# In the latter case, because φ(n) is not greater than n, f(n) = φ(n).
# Therefore g(n) = φ(1) + φ(3) + ... + φ(n-1),
# 
# Let P(n) = φ(1) + φ(2) + ... + φ(n) be the phi summatory function. Then:
#   g(n) = P(n) - [φ(2) + φ(4) + ... + φ(n)]
#        = P(n) - [φ(2) + φ(6) + ... + φ(n-2)] - [φ(4) + φ(8) + ... + φ(n)]
#        = P(n) - [φ(1) + φ(3) + ... + φ(n/2-1)] - 2[φ(2) + φ(4) + ... + φ(n/2)]
#        = P(n) - g(n/2) - 2[φ(2) + φ(4) + ... + φ(n/2)]
#        = P(n) - g(n/2) - 2g(n/4) - 4[φ(4) + φ(8) + ... + φ(n)]
#        = ...
#        = P(n) - g(n/2) - 2g(n/4) - 4g(n/8) - 8g(n/16) - ...
# Applying this formula to itself yields
#   g(n) = P(n) - P(n/2) - g(n/4) - 2g(n/8) - 4g(n/16) - ...
#        = P(n) - P(n/2) - P(n/4) -  g(n/8) - 2g(n/16) - ...
#        = ...
#        = P(n) - P(n/2) - P(n/4) - P(n/8) - P(n/16) - ...
# 
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

def solve(cap = 5 * 10 ** 8):
	memos = {1: 1}
	result = get_p(cap, memos)
	arg = cap
	while arg:
		arg //= 2
		result -= get_p(arg, memos)
	return result

if __name__ == "__main__":
	start = time()
	peresult(512, solve(), time() - start)
