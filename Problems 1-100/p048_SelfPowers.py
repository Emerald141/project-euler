# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 1000, mod = 10 ** 10):
    result = 0
    for num in range(1, cap + 1):
        result += pow(num, num, mod)
        result %= mod
    return result

if __name__ == "__main__":
    start = time()
    peresult(48, solve(), time() - start)
