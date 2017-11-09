##You are given a unique investment opportunity.
##
##Starting with £1 of capital, you can choose a
##fixed proportion, f, of your capital to bet on a
##fair coin toss repeatedly for 1000 tosses.
##
##Your return is double your bet for heads and you
##lose your bet for tails.
##
##For example, if f = 1/4, for the first toss you bet
##£0.25, and if heads comes up you win £0.5 and so
##then have £1.5. You then bet £0.375 and if the
##second toss is tails, you have £1.125.
##
##Choosing f to maximize your chances of having at
##least £1,000,000,000 after 1,000 flips, what is
##the chance that you become a billionaire?
##
##All computations are assumed to be exact (no
##rounding), but give your answer rounded to 12 digits
##behind the decimal point in the form 0.abcdefghijkl.

from time import time
from peresult import peresult
from probability import choose

def pe267():
        start = time()
        totalInsts = 0
        goodInsts = 0
        for tossesWon in range(1001):
                newInsts = choose(1000, tossesWon)
                totalInsts += newInsts
                if tossesWon > 333:
                        goodInsts += newInsts
        for tossesWon in range(334, 1001):
                bestBet = (3 * tossesWon - 1000) / 2000 #Hand-computed formula
                maxWinnings = (1 + 2 * bestBet) ** tossesWon * (1 - bestBet) ** (1000 - tossesWon)
                if maxWinnings < 10 ** 9:
                        goodInsts -= choose(1000, tossesWon)
                else:
                        break
        result = goodInsts / totalInsts
        result *= 10 ** 13
        result = round(result, -1)
        result /= 10 ** 13
        peresult(267, result, time() - start)

if __name__ == "__main__":
        pe267()
