##Taking three different letters from the 26 letters of the alphabet,
##character strings of length three can be formed.
##Examples are 'abc', 'hat' and 'zyx'.
##When we study these three examples we see that for 'abc' two characters
##come lexicographically after its neighbour to the left.
##For 'hat' there is exactly one character that comes lexicographically
##after its neighbour to the left. For 'zyx' there are zero characters
##that come lexicographically after its neighbour to the left.
##In all there are 10400 strings of length 3 for which exactly one character
##comes lexicographically after its neighbour to the left.
##
##We now consider strings of n ≤ 26 different characters from the alphabet.
##For every n, p(n) is the number of strings of length n for which exactly
##one character comes lexicographically after its neighbour to the left.
##
##What is the maximum value of p(n)?

from time import time
from peresult import peresult
from probability import choose

def pe158():
    start = time()
    chose = [ [choose(x, y) for y in range(x+1)] for x in range(25)]
    pOfN = [0 for x in range(27)]
    for p1 in range(25):
        for p2 in range(p1+1, 26):
            for countA in range(p1+1):
                probA = chose[p1][countA]
                for countB in range(p2 - p1):
                    probB = chose[p2 - p1 - 1][countB] * (2 ** countB)
                    for countC in range(26 - p2):
                        probC = chose[25 - p2][countC]
                        pOfN[countA+countB+countC] += probA*probB*probC
    print(pOfN)
    peresult(158, max(pOfN), time() - start)

if __name__ == "__main__":
    pe158()
