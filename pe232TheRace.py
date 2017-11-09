##Two players share an unbiased coin and take it in turns to play
##"The Race". On Player 1's turn, he tosses the coin once: if it
##comes up Heads, he scores one point; if it comes up Tails, he
##scores nothing. On Player 2's turn, she chooses a positive
##integer T and tosses the coin T times: if it comes up all Heads,
##she scores 2 ** (T-1) points; otherwise, she scores nothing. Player 1
##goes first. The winner is the first to 100 or more points.
##
##On each turn Player 2 selects the number, T, of coin tosses that
##maximises the probability of her winning.
##
##What is the probability that Player 2 wins?
##
##Give your answer rounded to eight decimal places in
##the form 0.abcdefgh .

##------------------------------------------------------------------
##Explanation for how this program works:
##
##Define f(a, b, c) as the probability of player 2 winning when
##P1 has a points, P2 has b points, c = 0 when it's P1's turn
##and c = 1 when it's p2's turn.
##
##It should be clear that f(100, b, c) == 0 for all b and c, and
##f(a, 100, c) == 1 for all b and c.
##
##In the following formulae and program, 'n' is used instead of 'T'.
##
##By the rules of the game, for a, b in the range [0, 99]
##f(a, b, 0) = (1/2) * f(a+1, b, 1) + (1/2) * f(a, b, 1)
##f(a, b, 1) = 1/(2**n) * f(a, b+2**(n-1), 0) + (2**n-1)/(2**n) * f(a, b, 0)
##
##By solving these simultaneous equations, we can reach the result
##f(a, b, 0) = (2**n)/(2**n+1) * f(a+1, b, 1) + 1/(2**n+1) * f(a, b+2**(n-1), 0)
##f(a, b, 1) = (2**n-1)/(2**n+1) * f(a+1, b, 1) + 2/(2**n+1) * f(a, b+2**(n-1), 0)
##
##This can be used repeatedly to reach f(0, 0, 0), the result desired.

from time import time
from peresult import peresult

def pe232():
        start = time()
        f = []
        for x in range(101):
                f.append([[0, 0] for y in range(101)])
        for losingA in range(100):
                f[losingA][100] = [1, 1]
        for b in range(99, -1, -1):
                for a in range(99, -1, -1):
                        winningn = False
                        n = 0 #gets augmented to 1 immediately
                        bestn = 0
                        bestprob = 0
                        bestdestb = 0
                        while not winningn:
                                n += 1
                                if b + 2 ** (n - 1) >= 100:
                                        winningn = True
                                        destb = 100
                                else:
                                        destb = b + 2 ** (n-1)
                                losingnum = (2 ** n - 1) * f[a+1][b][1]
                                winningnum = 2 * f[a][destb][0]
                                denom = 2 ** n + 1
                                prob = (losingnum + winningnum) / denom
                                if prob > bestprob:
                                        bestprob = prob
                                        bestdestb = destb
                                        bestn = n
                        f[a][b][1] = bestprob
                        losingnum = 2 ** bestn * f[a+1][b][1]
                        winningnum = f[a][bestdestb][0]
                        denom = 2 ** bestn + 1
                        f[a][b][0] = (losingnum + winningnum) / denom
        result = f[0][0][0]
        #Round result to eight decimal places
        result *= 10 ** 9
        result = round(result, -1)
        result /= 10 ** 9
        peresult(232, result, time() - start)

if __name__ == "__main__":
        pe232()
