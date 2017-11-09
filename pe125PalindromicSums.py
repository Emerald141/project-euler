##The palindromic number 595 is interesting because it can be written as
##the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
##
##There are exactly eleven palindromes below one-thousand that can be written
##as consecutive square sums, and the sum of these palindromes is 4164.
##Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned
##with the squares of positive integers.
##
##Find the sum of all the numbers less than 10^8 that are both palindromic
##and can be written as the sum of consecutive squares.

from time import time
from peresult import peresult

def pe125(cap):
    start = time()
    #Construct a list of eight-or-fewer-digit primes
    palindromes = set()
    for a in range(1, 10): #No leading zeros allowed
        palindromes.add(a) #1-digit palindromes
        palindromes.add(a * 11) #2-digit palindromes
        for b in range(10):
            palindromes.add(a * 101 + b * 10) #3-digit
            palindromes.add(a * 1001 + b * 110) #4-digit
            for c in range(10):
                palindromes.add(a * 10001 + b * 1010 + c * 100) #5-digit
                palindromes.add(a * 100001 + b * 10010 + c * 1100) #6-digit
                for d in range(10):
                    palindromes.add(a*1000001 + b*100010 + c*10100 + d*1000) #7
                    palindromes.add(a*10000001 + b*1000010 + c*100100 \
                                    + d*11000) #8-digit
    reachables = set() #Palindromes that are the sum of consecutive squares
    #Keep a list of squaresums where the last term is the term in question
    squaresums = set()
    for x in range(2, int(cap ** .5) + 1):
        squaresumsNew = set()
        for squaresum in squaresums:
            if squaresum + x**2 < cap:
                squaresumsNew.add(squaresum + x**2)
        squaresumsNew.add( (x-1)**2 + x**2 )
        for squaresumNew in squaresumsNew:
            if squaresumNew in palindromes:
                reachables.add(squaresumNew)
        squaresums = squaresumsNew
    result = sum(reachables)
    peresult(125, result, time() - start)

if __name__ == "__main__":
    pe125(10**8)
