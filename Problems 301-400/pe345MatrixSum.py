##We define the Matrix Sum of a matrix as the maximum sum of matrix
##elements with each element being the only one in his row and column.
##For example, the Matrix Sum of the matrix below equals
##3315 ( = 863 + 383 + 343 + 959 + 767):
##
smallmat = """\
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303"""
##
##Find the Matrix Sum of:
##
largemat = """\
  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"""

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(matrixString):
    start = time()
    
    # Set up the matrix by splitting the string
    matrix = matrixString.split('\n')
    for row in range(len(matrix)):
        matrix[row] = matrix[row].split(' ')
        for col in range(len(matrix[row]) - 1, -1, -1):
            if matrix[row][col] == '':
                del matrix[row][col]
            else:
                matrix[row][col] = int(matrix[row][col])

    # Dynamic programming:
    # Let the matrix sum of rows a1, a2, a3, ... an (sorted)
    # be the matrix sum of the nxn matrix formed by
    # taking the first n elements of each of those rows.
    # A unique key can be constructed:
    # key = 2^a1 + 2^a2 + 2^a3 + ... + 2^an
    # Using this key will help identify previously solved subproblems.
    
    ms = [-1 for x in range(2 ** len(matrix))]
    ms[0] = 0 # The matrix sum of a 0x0 submatrix is 0.
    def findms(key):
        # Have we solved this problem already?
        if ms[key] != -1:
            return ms[key]
        # Decode the key to find out which rows are covered.
        includedRows = []
        for row in range(len(matrix)):
            if (key // (2 ** row)) % 2 == 1:
                includedRows.append(row)
        # For each row in the nxn submatrix, take the element of the n'th
        # column and add the matrix sum of the other rows.
        # Whichever is largest - that's the new matrix sum.
        maxms = -1
        col = len(includedRows) - 1
        for row in includedRows:
            newms = matrix[row][col] + findms(key - (2 ** row))
            maxms = max(maxms, newms)
        # Save the answer to this subproblem.
        ms[key] = maxms
        return maxms

    # We want the matrix sum of all the rows.
    # The key for this will be 2^0 + 2^1 + 2^... + 2^(rowcount - 1)
    # a.k.a. 2^rowcount - 1.
    result = findms(2 ** len(matrix) - 1)
    peresult(345, result, time() - start)

if __name__ == "__main__":
    solve(largemat)
