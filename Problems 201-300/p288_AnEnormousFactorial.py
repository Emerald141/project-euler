# For any prime p the number N(p,q) is defined by N(p,q) = ∑(n=0 to q) T_n*p^n
# with T_n generated by the following random number generator:
# 
# S_0 = 290797
# S_(n+1) = S_n^2 mod 50515093
# T^n = S_n mod p
# 
# Let Nfac(p,q) be the factorial of N(p,q).
# Let NF(p,q) be the number of factors p in Nfac(p,q).
# 
# You are given that NF(3,10000) mod 3^20=624955285.
# 
# Find NF(61,10^7) mod 61^10.

# THEORY:
# 
# N(p,q) is a (q+1)-digit number in base p.
# As an illustration, consider the base 7 number n = 3265314;
# then the number of factors 7 in n! is
#	326531 + 32653 + 3265 + 326 + 32 + 3
# which is equivalent to
# 	1 + 33 + 555 + 6666 + 22222 + 333333.
# Thus the result is equivalent to the sum of T_n * r(n),
# where r(n) is the n-digit repunit in base p.
# If we're taking the result mod p^e, then these repunits all become the same
# after the first e.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(p = 61, q = 10 ** 7, e = 10):
	mod = p ** e
	result = 0
	s = 290797
	repunit = 0
	for n in range(1, e + 1):
		repunit += p ** (n - 1)
		s = pow(s, 2, 50515093)
		result += (s % p) * repunit
	for n in range(e + 1, q + 1):
		s = pow(s, 2, 50515093)
		result += (s % p) * repunit
		result %= mod
	return result

if __name__ == "__main__":
	start = time()
	peresult(288, solve(), time() - start)
