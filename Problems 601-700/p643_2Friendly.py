# Two positive integers a and b are 2-friendly when gcd(a,b)=2^t, t>0.
# For example, 24 and 40 are 2-friendly because gcd(24,40)=8=2^3
# while 24 and 36 are not because gcd(24,36)=12=2^2*3 not a power of 2.
# 
# Let f(n) be the number of pairs, (p,q), of positive integers with 1≤p<q≤n
# such that p and q are 2-friendly.
# You are given f(10^2)=1031 and f(10^6)=321418433 modulo 1000000007.
# 
# Find f(10^11) modulo 1000000007.

# THEORY:
# 
# If gcd(p,q) = 2^k, then p=a*2^k and q=b*2^k, where a and b are coprime
# positive integers less than N/(2^k), where N is the cap.
# There are P(N/(2^k)) such pairs (a,b), including the inadmissible pair (1,1),
# where P is the totient summatory function.
# The problem therefore becomes finding
# P(N/2) + P(N/4) + P(N/8) + ...
# and subtracting the number of nonzero terms in that sum.
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
from math import log

def get_p(n, memos, mod):
	if n in memos:
		return memos[n]
	result = (n * (n + 1) // 2) % mod
	denom = 2
	while denom <= n:
		arg = n // denom
		new_denom = n // arg + 1
		result -= get_p(arg, memos, mod) * (new_denom - denom)
		result %= mod
		denom = new_denom
	memos[n] = result
	return result	

def solve(cap = 10 ** 11, mod = 1000000007):
	memos = {1: 1}
	result = -int(log(cap, 2))
	while cap:
		cap //= 2
		result += get_p(cap, memos, mod)
		result %= mod
	return result

if __name__ == "__main__":
	start = time()
	peresult(643, solve(), time() - start)
