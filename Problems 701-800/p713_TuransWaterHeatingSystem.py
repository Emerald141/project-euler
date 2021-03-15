def binom2(x):
	return (x * (x - 1)) // 2

from math import ceil
result = 0
n = 10 ** 7
for r in range(1, n):
	result += (n % r) * binom2(ceil(n/r)) + (r - (n % r)) * binom2(n//r)
print(result)