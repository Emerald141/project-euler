##A unitary divisor d of a number n is a divisor of n that has
##the property gcd(d, n/d) = 1.
##The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
##The sum of their squares is 12 + 32 + 82 + 242 = 650.
##
##Let S(n) represent the sum of the squares of the unitary
##divisors of n. Thus S(4!)=650.
##
##Find S(100 000 000!) modulo 1 000 000 009.

from time import time
from peresult import peresult
from primefns import primesbelow

def pe429(cap, mod):
    start = time()
    primes = primesbelow(cap) #this is gonna take forever
    print("Finished finding primes, took", time() - start, "seconds")
    result = 1
    for p in primes:
        exponent = findExponent(p, cap)
        result *= powerMod(p, 2*exponent, mod) + 1
        result %= mod
    peresult(429, result, time() - start)

def findExponent(prime, cap):
    if cap == 0:
        return 0
    return (cap // prime) + findExponent(prime, cap // prime)

def powerMod(base, expRaw, mod):
    exp = bin(expRaw)[2:]
    x = 1
    power = base % mod
    for i in range(len(exp)-1, -1, -1):
        if exp[i] == '1':
            x = (x * power) % mod
        power = (power * power) % mod
    return x

if __name__ == "__main__":
    pe429(10**8, 1000000009)
