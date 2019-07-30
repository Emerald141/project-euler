# If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.
#
# The largest value of a such that a^2 ≡ a mod 6 is 4.
# Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).
# So M(6) = 4.
#
# Find ∑M(n) for 1 ≤ n ≤ 10^7.

# THEORY:
#
# If the prime decomposition of n is p(1)^e(1) * p(2)^e(2) * ... * p(m)^e(m),
# then a^2 ≡ a mod n if and only if a^2 ≡ a mod p(k)^e(k) for all k.
# This is true if and only if a ≡ 0 mod p^k or a ≡ 1 mod p^k.
# It follows that there exist coprime integers x, y such that x * y = n
# and a ≡ 0 mod x and a = 1 mod y.
# If we know x and y, then a is unique, and is x * (x^(-1) mod y)
# = x * (x^(phi(y)-1) mod y).
# So for any n, we just have to find all x and y, then take the max a.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve(cap = 10 ** 7):
    # Step 1: Get prime decomposition and totient of all integers
    primes = primesbelow(cap + 1)
    decomp = [ [] for x in range(cap + 1)]
    totient = [x for x in range(cap + 1)]
    for p in primes:
        for mult in range(p, cap + 1, p):
            decomp[mult].append(p)
            totient[mult] = totient[mult] * (p - 1) // p
        power = p
        while power <= cap:
            power *= p
            for mult in range(power, cap + 1, power):
                decomp[mult][-1] = power
    # Step 2: For each integer, analyze all possible x and y, and take max a
    result = 0  # Skipping 1 because M(1) = 0
    for n in range(2, cap + 1):
        factors = [1]
        for d in decomp[n]:
            factors = factors + [d * f for f in factors]
        max_a = 0
        for x in factors:
            y = n // x
            max_a = max(max_a, x * pow(x, totient[y] - 1, y))
        result += max_a
    return result

if __name__ == "__main__":
    start = time()
    peresult(407, solve(), time() - start)
