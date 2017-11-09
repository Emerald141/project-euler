##A k-input binary truth table is a map from k input bits
##(binary digits, 0 [false] or 1 [true]) to 1 output bit.
##For example, the 2-input binary truth tables for the logical
##AND and XOR functions are:
##
##x	y	x AND y
##0	0	0
##0	1	0
##1	0	0
##1	1	1
##
##x	y	x XOR y
##0	0	0
##0	1	1
##1	0	1
##1	1	0
##
##How many 6-input binary truth tables, τ, satisfy the formula
##
##τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0
##
##for all 6-bit inputs (a, b, c, d, e, f)?

from time import time
from peresult import peresult

def pe209():
    start = time()
    #Part 1: Create a set of all 6-bit inputs
    inputs = [0 for x in range(6)]
    inputset = set()
    index = len(inputs) - 1
    while True:
        if inputs[index] == 2:
            if index == 0:
                break
            else:
                inputs[index] = 0
                inputs[index - 1] += 1
                index -= 1
        else:
            index = len(inputs) - 1
            inputset.add(tuple(inputs))
            inputs[index] += 1
    #Part 2: Note what inputs chain around to each other
    thisChain = set()
    chainlengths = []
    visiting = next(iter(inputset))
    while True:
        if visiting in thisChain:
            chainlengths.append(len(thisChain))
            thisChain = set()
            if len(inputset) == 0:
                break
            else:
                visiting = next(iter(inputset))
        else:
            inputset.remove(visiting)
            thisChain.add(visiting)
            visiting = (visiting[1], visiting[2], visiting[3], visiting[4], \
                        visiting[5], visiting[0] ^ (visiting[1] and visiting[2]))
    #Part 3: Compute possibilities for each chain
    result = 1
    for chainlength in chainlengths:
        if chainlength == 1: #edge case
            continue
        #'casecount' works along each link of the chain
        #and keeps track of how many possible combinations of
        #the previous links could result in it being a 0, or
        #being a 1. The format is:
        #casecount[0] = first link 0, this link 0
        #casecount[1] = first link 0, this link 1 (next can't be 1)
        #casecount[2] = first link 1, this link 0
        #casecount[3] = first link 1, this link 1 (discard at end)
        casecount = [1, 1, 1, 0] #this is the second link
        for x in range(chainlength - 2): #Two links already accounted for
            casecount = [casecount[0] + casecount[1],   \
                         casecount[0],                  \
                         casecount[2] + casecount[3],   \
                         casecount[2]]
        result *= casecount[0] + casecount[1] + casecount[2]
    peresult(209, result, time() - start)

if __name__ == "__main__":
    pe209()
