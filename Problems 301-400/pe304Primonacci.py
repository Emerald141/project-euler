##For any positive integer n the function next_prime(n) returns the smallest prime p 
##such that p>n.
##
##The sequence a(n) is defined by:
##a(1)=next_prime(1014) and a(n)=next_prime(a(n-1)) for n>1.
##
##The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.
##
##The sequence b(n) is defined as f(a(n)).
##
##Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from primefns import primesbelow

def solve():
    start = time()
    mod = 1234567891011
    primes = primesbelow(10 ** 7 + 2)
    #Sieve represents numbers from 10**14 to 10**14+10**7-1
    sieve = [True for x in range(10 ** 7)]
    for p in primes:
        lowestMultiple = (10 ** 14) // p * p
        if lowestMultiple < 10 ** 14:
            lowestMultiple += p
        for multiple in range(lowestMultiple - 10 ** 14, len(sieve), p):
            sieve[multiple] = False
    primes = [] #Might as well reuse the array name
    for index in range(len(sieve)):
        if len(primes) >= 100000:
            break
        if sieve[index]:
            primes.append(index)
    matpows = [[1, 1, 1, 0]]
    for twopow in range(47): #just to be safe
        newmat = matrixmult(matpows[-1], matpows[-1])
        for index in range(len(newmat)):
            newmat[index] %= mod
        matpows.append(newmat)
    index1 = primes[0] + (10 ** 14) - 1
    matrix = [1, 1, 1, 0]
    while index1 > 0:
        power = 0
        while 2 ** (power + 1) < index1:
            power += 1
        matrix = matrixmult(matrix, matpows[power])
        index1 -= 2 ** power
    result = matrix[1]
    for index in range(1, len(primes)):
        stepsLeft = primes[index] - primes[index - 1]
        while stepsLeft > 0:
            power = 0
            while 2 ** (power + 1) < stepsLeft:
                power += 1
            matrix = matrixmult(matrix, matpows[power])
            for index in range(len(matrix)):
                matrix[index] %= mod
            stepsLeft -= 2 ** power
        result += matrix[1]
        result %= mod
    peresult(304, result, time() - start)

def matrixmult(mat1, mat2):
    #[a b]
    #[c d]
    #is recorded as [a b c d]
    result = []
    result.append(mat1[0] * mat2[0] + mat1[1] * mat2[2])
    result.append(mat1[0] * mat2[1] + mat1[1] * mat2[3])
    result.append(mat1[2] * mat2[0] + mat1[3] * mat2[2])
    result.append(mat1[2] * mat2[1] + mat1[3] * mat2[3])
    return result

if __name__ == "__main__":
    solve()
