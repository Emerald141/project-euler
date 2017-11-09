##Let n be a positive integer.
##A 6-sided die is thrown n times. Let c be the number of pairs of consecutive
##throws that give the same value.
##
##For example, if n = 7 and the values of the die throws are (1,1,5,6,6,6,3),
##then the following pairs of consecutive throws give the same value:
##(1,1,5,6,6,6,3)
##(1,1,5,6,6,6,3)
##(1,1,5,6,6,6,3)
##Therefore, c = 3 for (1,1,5,6,6,6,3).
##
##Define C(n) as the number of outcomes of throwing a 6-sided die n times such
##that c does not exceed pi(n) (where pi is the prime counting function).
##For example, C(3) = 216, C(4) = 1290, C(11) = 361912500
##and C(24) = 4727547363281250000.
##
##Define S(L) as ∑ C(n) for 1 ≤ n ≤ L.
##For example, S(50) mod 1 000 000 007 = 832833871.
##
##Find S(50 000 000) mod 1 000 000 007.

from time import time
from peresult import peresult
from primefns import primesbelow

def modInverse(x, mod):
    # Computation of modular inverse via extended Euclidean algorithm.
    if x <= 1: return x
    a = mod % x
    qMinusTwo = mod // x
    b = x % a
    qMinusOne = x // a
    pMinusTwo, pMinusOne = 0, 1
    while b != 0:
        pMinusTwo, pMinusOne = pMinusOne, \
                               (pMinusTwo - qMinusTwo * pMinusOne) % mod
        qMinusTwo = qMinusOne
        qMinusOne = a // b
        a, b = b, a % b
    return (pMinusTwo - qMinusTwo * pMinusOne) % mod

def pe423(cap):
    start = time()
    mod = 1000000007
    primes = primesbelow(cap + 1)
    for x in range(len(primes)):
        primes[x] -= 1
    # Disregard the first die roll and define pi(n) as pi(n-1).
    c = 6 # Number of counts of AT MOST pi(n) rolls. This is c(0).
    e = 6 # Number of counts of EXACTLY pi(n) rolls. This is e(0).
    pi = 0 # The redefined pi(n). This is pi(0).
    result = 6 # Sum thus far of c
    for n in range(1, cap):
        if len(primes) != 0 and primes[0] == n: #if n is prime
            pi += 1
            del primes[0]
            eNew = (e * n * modInverse(pi, mod)) % mod
            c = 6 * c - e + eNew
            e = eNew
        else: #if n is not prime
            c = 6 * c - e
            e = (e * 5 * n * modInverse(n - pi, mod)) % mod
        result += c
        result %= mod
        if n % 100 == 0:
            print(n, result, time() - start, sep='\t')
    peresult(423, result, time() - start)

if __name__ == "__main__":
    pe423(50000000)
