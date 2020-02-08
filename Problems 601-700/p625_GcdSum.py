# G(N) = sum of gcd(i,j), for 1 <= i <= j <= N.
# You are given: G(10)=122.
# 
# Find G(10^11). Give your answer modulo 998244353

# THEORY:
# 
# G(N) = sum of (k * number of 1 <= i <= j <= N with gcd(i,j)=k) over k
#      = sum of (k * number of 1 <= i <= j <= N/k with gcd(i,j)=1) over k
#      = sum of (k * P(N/k)) over k
# where P is the totient summatory function.

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

def solve(cap = 10 ** 11, mod = 998244353):
    memos = {1: 1}
    result = 0
    k = 1
    while k <= cap:
        p = get_p(cap // k, memos, mod)
        new_k = (cap // (cap // k)) + 1
        result += (new_k * (new_k - 1) - k * (k - 1)) // 2 * p
        result %= mod
        k = new_k
    return result

if __name__ == "__main__":
    start = time()
    peresult(625, solve(), time() - start)
