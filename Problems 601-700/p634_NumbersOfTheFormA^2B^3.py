# Define F(n) to be the number of integers x≤n that can be written in the form
# x=a^2*b^3, where a and b are integers not necessarily different and both
# greater than 1.
#
# For example, 32=2^2*2^3 and 72=3^2*2^3 are the only two integers less than
# 100 that can be written in this form. Hence, F(100)=2.
#
# Further you are given F(2*10^4)=130 and F(3*10^6)=2014.
#
# Find F(9*10^18).

# THEORY:
# This representation is unique if we require b to be either squarefree or
# the square of a prime, and in the latter case, if we require p^3 does not
# divide a for any prime p < b. We can figure this last condition out by
# inclusion-exclusion (strategy borrowed from problem 268).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def subproduct(array, indices):
	product = 1
	for index in indices:
		product *= array[index]
	return product

def solve(cap = 9 * 10 ** 18):
	max_b = int((cap/4) ** (1/3))
	is_prime = [False, False] + [True for b in range(2, max_b + 1)]
	is_squarefree = [False, False] + [True for b in range(2, max_b + 1)]
	prime_cubes = []
	result = 0
	test = set()
	for b in range(2, max_b + 1):
		if is_prime[b]:
			# Mark all multiples of b as not being prime
			for mult in range(2 * b, max_b + 1, b):
				is_prime[mult] = False
			# Mark all multiples of b^2 as not being squarefree
			for squaremult in range(b ** 2, max_b + 1, b ** 2):
				is_squarefree[squaremult] = False
			# Analyze case where the square of b gets plugged in
			max_a = int(sqrt(cap // (b ** 6)))
			if max_a >= 2:
				result += max_a - 1  # 1 doesn't work
				# Use inclusion-exclusion to see how many numbers work
				for length in range(1, len(prime_cubes) + 1):
					indices = [i for i in range(length)]
					while True:
						term = max_a // subproduct(prime_cubes, indices)
						result += ((-1) ** length) * term
						if term != 0 and indices[-1] != len(prime_cubes) - 1:
							indices[-1] += 1
							continue
						for i in range(len(indices) - 2, -1, -1):
							if indices[i] + 1 != indices[i + 1]:
								for j in range(len(indices) - 1, i - 1, -1):
									indices[j] = indices[i] + j - i + 1
								break
						else:
							# We've found all we can for this length
							break
				if b ** 3 <= cap:
					prime_cubes.append(b ** 3)
		if is_squarefree[b]:
			max_a = int(sqrt(cap // (b ** 3)))
			result += max_a - 1
	return result

if __name__ == "__main__":
	start = time()
	peresult(634, solve(), time() - start)
