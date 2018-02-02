##A deck of cards numbered from 1 to n is shuffled randomly such that each
##permutation is equally likely.
##
##The cards are to be sorted into ascending order using the following
##technique:
##
##Look at the initial sequence of cards. If it is already sorted, then
##there is no need for further action. Otherwise, if any subsequences of
##cards happen to be in the correct place relative to one another (ascending
##with no gaps), then those subsequences are fixed by attaching the cards
##together. For example, with 7 cards initially in the order 4123756, the
##cards labelled 1, 2 and 3 would be attached together, as would 5 and 6.
##The cards are 'shuffled' by being thrown into the air, but note that any
##correctly sequenced cards remain attached, so their orders are maintained.
##The cards (or bundles of attached cards) are then picked up randomly. You
##should assume that this randomisation is unbiased, despite the fact that
##some cards are single, and others are grouped together.
##Repeat steps 1 and 2 until the cards are sorted.
##Let S(n) be the expected number of shuffles needed to sort the cards.
##Since the order is checked before the first shuffle, S(1) = 0. You are
##given that S(2) = 1, and S(5) = 4213/871.
##
##Find S(52), and give your answer rounded to 8 decimal places.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def arrayAdd(arrayA, arrayB):
    return [arrayA[i] + arrayB[i] for i in range(len(arrayA))]

for x in range(1):
    deckSize = 5
    #Define a "run" as a consecutive grouping of one or more ascending cards.
    start = time()
    #Dictionary where each argument is a 2-tuple of an int and a list of ints.
    #The first element represents the possible cards that the current run
    #could be extended by.
    #The second element represents the other possible runs that could be
    #placed in the future, with each element the length of a possible run.
    #So, for example, if we were working with the digits 123456789 and
    #the previously laid digits were 647, the remaining elements in the
    #current run would be 89, and the other remaining runs would be
    #123 and 5. Thus the corresponding tuple would be (2, [1, 3]).
    #The value associated with this key is an array A,
    #where A[n] is the number of configurations with n runs
    #(discounting the ones already in the sequence).
    runcount = {(0, tuple()): (1,) + tuple([0 for i in range(deckSize)])}
    #Null case - if no cards left, no runs left

    def findValue(key):
        print('key =', key)
        if key in runcount:
            print("Early return. result =", runcount[key])
            return runcount[key] #Hooray for DP!
        currentRun = key[0]
        otherRuns = key[1]        
        result = [0 for i in range(deckSize + 1)]
        if currentRun > 0:
            print("Adding continuation of current run:")
            result = findValue((currentRun - 1, otherRuns))
            print("Temp result X =", result)
            for m in range(2, currentRun + 1):
                print('m =', m)
                result = arrayAdd( result, (0,) + findValue(( currentRun - m, tuple(sorted(otherRuns + (m - 1,) )) ))[:-1] )
                print("Temp result Y =", result)
        for i in range(len(otherRuns)):
            print('i =', i)
            newOtherRuns = otherRuns[:i] + (currentRun,) + otherRuns[i+1:] #to keep the original
            if currentRun == 0:
                newOtherRuns = otherRuns[:i] + otherRuns[i+1:]
            print('newOtherRuns =', newOtherRuns)
            newRunLength = otherRuns[i]
            print('newRunLength =', newRunLength)
            for k in range(newRunLength - 1):
                print('k =', k)
                result = arrayAdd( result, (0,) + findValue(( k, tuple(sorted(newOtherRuns + (newRunLength - k - 1,))) ))[:-1] )
                print("Temp result A =", result)
            if newRunLength > 0:
                print("Final addition")
                result = arrayAdd( result, (0,) + findValue(( newRunLength - 1, tuple(sorted(newOtherRuns)) ))[:-1] )
                print("Temp result B =", result)
        result = tuple(result)
        runcount[key] = result
        print("result =", result)
        return result

findValue((0, (5,)))




                                    
