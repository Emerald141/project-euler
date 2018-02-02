##Consider graphs built with the units A:  and B: , where the units
##are glued along the vertical edges as in the graph, which can be found
##online because I can't paste images into Python (duh).
##
##A configuration of type (a,b,c) is a graph thus built of a units A and
##b units B, where the graph's vertices are coloured using up to c colours,
##so that no two adjacent vertices have the same colour.
##The compound graph above is an example of a configuration of type (2,2,6),
##in fact of type (2,2,c) for all c ≥ 4.
##
##Let N(a,b,c) be the number of configurations of type (a,b,c).
##For example, N(1,0,3) = 24, N(0,2,4) = 92928 and N(2,2,3) = 20736.
##
##Find the last 8 digits of N(25,75,1984).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(a, b, c):
    start = time()
    combosA, combosB = 0, 0
    for col0 in [1, -2]:
        for col1 in [1, 2, -2]:
            for col2 in [1, 2, 3, -1, -2]:
                for col3 in [1, 2, 3, 4, -1]:
                    for col4 in [1, 2, 3, 4, 5, -1, -2]:
                        if col1 == col0:
                            continue
                        if col1 > max(0, col0) + 1:
                            continue
                        if col2 == col1:
                            continue
                        if col2 > max(col0, col1) + 1:
                            continue
                        if col3 == col2:
                            continue
                        if col3 > max(col0, col1, col2) + 1:
                            continue
                        if col4 == col3 or col4 == col0:
                            continue
                        if col4 > max(col0, col1, col2, col3) + 1:
                            continue
                        if max(col0, col1, col2, col3, col4) > c - 2:
                            continue
                        setupCount = 1
                        for i in range(max(col0, col1, col2, col3, col4)):
                            setupCount *= c - 2 - i
                        combosB += setupCount
                        if col4 != -2:
                            combosA += setupCount
    currentCombos = [c * (c-1)] + [0 for x in range(b)]
    for step in range(a + b):
        currentCombos = [combosA * currentCombos[0]] \
            + [combosA * currentCombos[i] + combosB * currentCombos[i-1] \
               for i in range(1, b+1)]
    result = currentCombos[-1] % 10**8
    peresult(194, result, time() - start)

if __name__ == "__main__":
    solve(25, 75, 1984)
