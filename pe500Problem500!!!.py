##The number of divisors of 120 is 16.
##In fact 120 is the smallest number having 16 divisors.
##
##Find the smallest number with 2 ^ 500500 divisors.
##Give your answer modulo 500500507.

from time import time
from peresult import peresult
from primefns import primesbelow, primeabove

def pe500():
        start = time()
        terminalprime = 7376507 #500500th prime
        powercols = [primesbelow(terminalprime + 1)]
        while True:
                powercols.append([])
                sniprow = len(powercols[0]) - 1
                newrow = 0
                while True:
                        possiblenew = powercols[0][newrow] ** (2 ** (len(powercols) - 1))
                        if powercols[0][sniprow] > possiblenew:
                                del powercols[0][sniprow]
                                powercols[-1].append(possiblenew)
                                newrow += 1
                                sniprow -= 1
                        else:
                                break
                if newrow == 0:
                        break
        result = 1
        for col in range(len(powercols)):
                for row in range(len(powercols[col])):
                        result *= powercols[col][row]
                        result %= 500500507
        peresult(500, result, time() - start)

if __name__ == "__main__":
        pe500()
