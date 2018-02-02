##The Golomb's self-describing sequence {G(n)} is the only nondecreasing
##sequence of natural numbers such that n appears exactly G(n) times in
##the sequence. The values of G(n) for the first few n are
##
##n	1	2	3	4	5	6	7	8	9
##G(n)	1	2	2	3	3	4	4	4	5
##You are given that G(10^3) = 86, G(10^6) = 6137.
##You are also given that ΣG(n^3) = 153506976 for 1 ≤ n < 10^3.
##
##Find ΣG(n^3) for 1 ≤ n < 10^6.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap):
    start = time()
    # This program uses a 3-stage system for calculating large G(n).
    # STAGE 1:
    #   A generating list. For each index i, the value at i is
    #   the largest n for which G(n) = i. So the list would start
    #   [0, 1, 3, 5, 8, 11, ...]
    #   This list keeps a pointer to its earlier entries so it knows
    #   how much to expand itself by when necessary.
    #   Previous values are stored out of time necessity.
    # STAGE 2:
    #   A "short seeker". A pair of ints representing an index and value
    #   for the generating list, but NOT stored in the Stage 1 list.
    #   References the final element in the generating list to know
    #   how much to expand by at each iteration.
    # STAGE 3:
    #   A "long seeker". A pair of an index and value, like the short
    #   seeker. However, the long seeker takes information from the short
    #   seeker and increases the index manyfold in each loop.
    #   This is where G(n^3) values are found.

    # SETUP - STAGE 1
    genList = [0, 1, 3] # The generating list
    genListPointer = 2  # A pointer for use in expanding the list. If the
                        # number of elements is less than the value at the
                        # pointer, then make the new entry equal to the
                        # previous final entry plus the pointer's index.
                        # Else, increase the pointer first.
    # SETUP - STAGE 2
    shortSeekerIndex = 2
    shortSeekerValue = 3
    # SETUP - STAGE 3
    # At index 5, the values of genList stop going up by 3.
    # At index 8, they stop going up by 4.
    # The long seeker increaser is augmented with each loop
    # and references the short seeker, to see how long the pattern
    # of increasing by that constant continues.
    longSeekerIndex = 5
    longSeekerValue = 11
    longSeekerIncreaser = 3
    # SETUP - MISC
    result = 5 # G(1^3) + G(2^3) = 1 + 4 = 5
    base = 3 #The lowest n for which G(n^3) has not been found

    # MAIN LOOP
    while base < cap:
        longSeekerIncreaser += 1
        if longSeekerIncreaser > shortSeekerValue:
            # Need to increase the short seeker index
            if shortSeekerIndex < genList[-1]:
                # No need to expand the genList.
                shortSeekerIndex += 1
                shortSeekerValue += len(genList) - 1
            else:
                # genList needs to be expanded.
                # Taking care of the short seeker first:
                shortSeekerIndex += 1
                shortSeekerValue += len(genList)
                # Now let's check if the genListPointer needs to be moved up
                if len(genList) <= genList[genListPointer]:
                    # No need to advance the pointer
                    genList.append(genList[-1] + genListPointer)
                else:
                    # Must advance the pointer
                    genListPointer += 1
                    genList.append(genList[-1] + genListPointer)
        longSeekerValueNew = longSeekerValue + \
                             longSeekerIncreaser * shortSeekerIndex
        while longSeekerValueNew > base ** 3 and base < cap:
            result += longSeekerIndex + 1 + \
                      (base ** 3 - longSeekerValue - 1) // longSeekerIncreaser
            #print("New result:", base ** 3, longSeekerIndex + 1 + \
            #          (base ** 3 - longSeekerValue - 1) // longSeekerIncreaser)
            base += 1
        longSeekerValue = longSeekerValueNew
        longSeekerIndex += shortSeekerIndex
        #print(shortSeekerIndex, shortSeekerValue, longSeekerIndex, longSeekerValue, longSeekerIncreaser, sep='\t')
    peresult(341, result, time() - start)

if __name__ == "__main__":
    solve(10**6)
