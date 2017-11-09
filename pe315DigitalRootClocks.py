##Sam and Max are asked to transform two digital clocks into two
##"digital root" clocks.
##A digital root clock is a digital clock that calculates digital roots
##step by step.
##
##When a clock is fed a number, it will show it and then it will start the
##calculation, showing all the intermediate values until it gets to the result.
##For example, if the clock is fed the number 137, it will show:
##"137" → "11" → "2" and then it will go black, waiting for the next number.
##
##Every digital number consists of some light segments: three horizontal
##(top, middle, bottom) and four vertical (top-left, top-right, bottom-left,
##bottom-right).
##Number "1" is made of vertical top-right and bottom-right, number "4" is
##made by middle horizontal and vertical top-left, top-right and bottom-right.
##Number "8" lights them all.
##
##The clocks consume energy only when segments are turned on/off.
##To turn on a "2" will cost 5 transitions, while a "7" will cost only 4
##transitions.
##
##Sam and Max built two different clocks.
##
##Sam's clock is fed e.g. number 137: the clock shows "137", then the panel
##is turned off, then the next number ("11") is turned on, then the panel is
##turned off again and finally the last number ("2") is turned on and, after
##some time, off.
##For the example, with number 137, Sam's clock requires:
##
##"137"	:	(2 + 5 + 4) × 2 = 22 transitions ("137" on/off).
##"11"	:	(2 + 2) × 2 = 8 transitions ("11" on/off).
##"2"	:	(5) × 2 = 10 transitions ("2" on/off).
##For a grand total of 40 transitions.
##Max's clock works differently. Instead of turning off the whole panel, it is
##smart enough to turn off only those segments that won't be needed for the
##next number.
##For number 137, Max's clock requires a grand total of 30 transitions.
##Of course, Max's clock consumes less power than Sam's one.
##The two clocks are fed all the prime numbers between A = 10^7 and B = 2×10^7. 
##Find the difference between the total number of transitions needed by Sam's
##clock and that needed by Max's one.

from time import time
from peresult import peresult
from digitfns import digitsum, digitcount

lights = [ [] for x in range(10)]

def pe315():
        start = time()
        sieve = [True for x in range(2 * 10 ** 7)]
        checkedCap = int((2 * 10 ** 7) ** .5) + 2
        for ind in range(2, checkedCap):
                if sieve[ind]:
                        for multiple in range(2 * ind, len(sieve), ind):
                                sieve[multiple] = False
        primes = []
        for ind in range(10 ** 7, len(sieve)):
                if sieve[ind]:
                        primes.append(ind)
        #Pattern: Three horizontal first, then four vertical
        #Top, Middle, Bottom, Northwest, Northeast, Southwest, Southeast
        lights[0] = [True, False, True, True, True, True, True]
        lights[1] = [False, False, False, False, True, False, True]
        lights[2] = [True, True, True, False, True, True, False]
        lights[3] = [True, True, True, False, True, False, True]
        lights[4] = [False, True, False, True, True, False, True]
        lights[5] = [True, True, True, True, False, False, True]
        lights[6] = [True, True, True, True, False, True, True]
        lights[7] = [True, False, False, True, True, False, True]
        lights[8] = [True, True, True, True, True, True, True]
        lights[9] = [True, True, True, True, True, False, True]
        grid = [ [] for x in range(100)]
        for a in range(len(grid)):
                for b in range(100):
                        grid[a].append(energyConserved(a, b) + energyConserved(b))
        result = 0
        for prime in primes:
                result += grid[prime % 100][digitsum(prime)]
        peresult(315, result, time() - start)

def energyConserved(currentnum, endnum=-1):
        result = 0
        if endnum == -1:
                nextnum = digitsum(currentnum)
                while currentnum != endnum and currentnum >= 10:
                        for place in range(digitcount(nextnum)):
                                currentDigit = currentnum // (10 ** place) % 10
                                nextDigit = nextnum // (10 ** place) % 10
                                for lightbar in range(len(lights[0])):
                                        if lights[currentDigit][lightbar] and lights[nextDigit][lightbar]:
                                                result += 2
                        currentnum = nextnum
                        nextnum = digitsum(currentnum)
                return result
        else:
                for place in range(digitcount(endnum)):
                        currentDigit = currentnum // (10 ** place) % 10
                        endDigit = endnum // (10 ** place) % 10
                        for lightbar in range(len(lights[0])):
                                if lights[currentDigit][lightbar] and lights[endDigit][lightbar]:
                                        result += 2
                return result

if __name__ == "__main__":
        pe315()
