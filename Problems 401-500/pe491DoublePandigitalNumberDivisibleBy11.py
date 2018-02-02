##We call a positive integer double pandigital if it uses all the
##digits 0 to 9 exactly twice (with no leading zero).
##For example, 40561817703823564929 is one such number.
##
##How many double pandigital numbers are divisible by 11?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    #Test if a number is divisible by 11:
    #Label all digits as follows.
    #+-+-+-+-+-+-+-+-+-+-
    #Sum the + digits, then subtract the - digits.
    #If the result is a mult of 11, the number is too.
    start = time()
    #This is my way of simulating ten nested for loops:
    digitCounts = [0 for x in range(10)] #How many are in the + spots
    index = 0
    result = 0
    factorial = [1, 1, 2]
    tenFactorial = 1
    for x in range(1, 11):
        tenFactorial *= x
    nineFactorial = tenFactorial // 10
    while True:
        if digitCounts[index] == 3:
            if index == 0:
                break
            else:
                digitCounts[index] = 0
                digitCounts[index - 1] += 1
                index -= 1
        else:
            index = len(digitCounts) - 1
            if sum(digitCounts) == 10: #10 positive digits, 10 negative
                positiveSum = sum(x * digitCounts[x] for x in range(10))
                if (positiveSum - 1) % 11 == 0: #pos - neg = 11k for some k
                    posCombos, negCombos = tenFactorial, tenFactorial
                    for x in range(len(digitCounts)):
                        posCombos //= factorial[digitCounts[x]]
                        negCombos //= factorial[2 - digitCounts[x]]
                    result += posCombos * negCombos
                    #And now to get rid of the numbers that start with 0
                    if digitCounts[0] > 0:
                        digitCounts[0] -= 1 #temporarily
                        posBadCombos = nineFactorial
                        for x in range(len(digitCounts)):
                            posBadCombos //= factorial[digitCounts[x]]
                        result -= posBadCombos * negCombos
                        digitCounts[0] += 1
            digitCounts[index] += 1
    peresult(491, result, time() - start)

if __name__ == "__main__":
    solve()
