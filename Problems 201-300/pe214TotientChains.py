##Let φ be Euler's totient function, i.e. for a natural number n,
##φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.
##
##By iterating φ, each positive integer generates a decreasing chain
##of numbers ending in 1.
##E.g. if we start with 5 the sequence 5,4,2,1 is generated.
##Here is a listing of all chains with length 4:
##
##5,4,2,1
##7,6,2,1
##8,4,2,1
##9,6,2,1
##10,4,2,1
##12,4,2,1
##14,6,2,1
##18,6,2,1
##
##Only two of these chains start with a prime, their sum is 12.
##
##What is the sum of all primes less than 40000000 which generate a
##chain of length 25?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap, chainlength):
    start = time()
    phi = [x for x in range(cap)]
    result = 0
    for x in range(2, len(phi)):
        if phi[x] != x: #if x is not prime (since decrement by 1 not done yet)
            continue
        for multiple in range(x, len(phi), x):
            phi[multiple] = phi[multiple] * (x-1) // x
        link = x
        for i in range(chainlength - 2):
            link = phi[link]
        if link != 1 and phi[link] == 1:
            result += x
    peresult(214, result, time() - start)

if __name__ == "__main__":
    solve(40000000, 25)
