# We define two sequences S = {S(1), S(2), ..., S(n)} and
# S_2 = {S_2(1), S_2(2), ..., S_2(n)}:
#
# S(k) = (p_k)^k mod 10007 where p_k is the kth prime number.
#
# S_2(k) = S(k) + S(floor(k / 10000) + 1).
#
# Then let M(i,j) be the median of elements S_2(i) through S_2(j), inclusive.
# For example, M(1,10) = 2021.5 and M(10^2,10^3) = 4715.0.
#
# Let F(n,k) = sum_{i=1}^{n-k+1} M(i,i+k-1). For example,
# F(100,10) = 463628.5 and F(10^5,10^4) = 675348207.5.
#
# Find F(10^7, 10^5). If the sum is not an integer, use .5 to denote a half.
# Otherwise, use .0 instead.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(n = 10 ** 7, k = 10 ** 5, mod=10007):
    primes = [0] + primesbelow(20 * n)  # avoiding index issues
    print("Found primes")
    S = [pow(primes[i], i, mod) for i in range(len(primes))]
    print("Created S")
    S2 = [S[i] + S[(i // 10000) + 1] for i in range(len(primes))]
    print("Created S2")
    # Populate initial data set
    vals = [0 for x in range(2 * mod - 1)]
    for i in range(1, k + 1):
        vals[S2[i]] += 1
    # Find initial medians
    remaining = k // 2
    for x in range(len(vals)):
        if vals[x] < remaining:
            remaining -= vals[x]
        else:
            low_med = [x, remaining]
            if remaining == vals[x]:
                high_med = [x+1, 1]
                while vals[high_med[0]] == 0:
                    high_med[0] += 1
            else:
                high_med = [x, remaining+1]
            break
    result = low_med[0] + high_med[0]
    # Rotate in elements of S2
    for i in range(k+1, n+1):
        old = S2[i-k]
        new = S2[i]
        vals[old] -= 1
        vals[new] += 1
        for med in (low_med, high_med):
            if new < med[0] and old >= med[0]:
                # Decrease the median
                if med[1] > 1:
                    med[1] -= 1
                else:
                    # Top of the next lowest stack
                    med[0] -= 1
                    while vals[med[0]] == 0:
                        med[0] -= 1
                    med[1] = vals[med[0]]
            elif (old < med[0] and new >= med[0]) or \
                 (old == med[0] and new > med[0] and vals[med[0]] < med[1]):
                # Increase the median
                if med[1] < vals[med[0]]:
                    med[1] += 1
                else:
                    # Bottom of the next highest stack
                    med[0] += 1
                    while vals[med[0]] == 0:
                        med[0] += 1
                    med[1] = 1
        result += low_med[0] + high_med[0]
        #print(vals, low_med, high_med, sep='\t')
    return result / 2

if __name__ == "__main__":
    start = time()
    peresult(593, solve(), time() - start)
