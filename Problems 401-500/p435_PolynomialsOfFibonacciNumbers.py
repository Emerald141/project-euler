# The Fibonacci numbers {f_n, n ≥ 0} are defined recursively as
# f_n = f_{n-1} + f_{n-2} with base cases f_0 = 0 and f_1 = 1.
#
# Define the polynomials {F_n, n ≥ 0} as F_n(x) = ∑f_i * x^i for 0 ≤ i ≤ n.
#
# For example, F_7(x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + 13x^7,
# and F_7(11) = 268357683.
#
# Let n = 10^15. Find the sum [∑0≤x≤100 F_n(x)] mod 1307674368000 (= 15!).

# THEORY:
#
# Let phi = (1 + sqrt(5)) / 2 and psi = (1 - sqrt(5)) / 2.
# Then f_n = (phi^n - psi^n) / sqrt(5).
# This turns f_i * x^i into a geometric series whose sum from 0 to n is
# (f_{n+1} * x^(n+1) + f_n * x*(n+2) - x) / (x^2 + x - 1).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

# Inputs two 2-tuples where (a,b) represents (a + b * sqrt(5)) / 2.
# Outputs a tuple representing their product in the same way.
def fibo_mult(pair1, pair2, mod):
    return ( (pair1[0] * pair2[0] + 5 * pair1[1] * pair2[1]) // 2 % mod, \
             (pair1[0] * pair2[1] + pair1[1] * pair2[0]) // 2 % mod )

def solve(n = 10 ** 15, x_cap = 100, mod_global = 1307674368000):
    result = 0
    for x in range(0, x_cap + 1):
        # The modulus must be scaled up by the denominator of the series sum,
        # so that the eventual division can be performed successfully.
        mod = mod_global * (x ** 2 + x - 1)

        # The first task is to find f_n and f_{n+1}.
        # The following list represents the integer and sqrt(5) terms in the
        # numerator of phi^(2^i), where i is the index. The terms in psi are the
        # same but with the sqrt(5) term sign reversed. The denominator is always 2.
        phis = [(1, 1)]
        while 2 ** len(phis) <= n:
            phis.append(fibo_mult(phis[-1], phis[-1], mod * 2))
        fibo_pair = (2, 0)  # Represents (2 + 0 * sqrt(5)) / 2, i.e. 1
        power_index = 0
        n_copy = n
        while n_copy > 0:
            if n_copy % 2 == 1:  # n's binary representation has a 1 at this index
                fibo_pair = fibo_mult(fibo_pair, phis[power_index], mod * 2)
            n_copy //= 2
            power_index += 1
        lesser_fibo = fibo_pair[1] % mod  # f_n
        greater_fibo = fibo_mult(phis[0], fibo_pair, mod * 2)[1] % mod

        # Now that we have f_n and f_{n+1}, we can find the series sum.
        result += (greater_fibo * pow(x, n + 1, mod) + lesser_fibo \
                    * pow(x, n + 2, mod) - x) // (x ** 2 + x - 1)
    return result % mod_global

if __name__ == "__main__":
    start = time()
    peresult(435, solve(), time() - start)
