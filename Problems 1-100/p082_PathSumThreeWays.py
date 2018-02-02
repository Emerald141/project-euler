##Find the minimal path sum, in matrix.txt, a 31K text file
##containing a 80 by 80 matrix, from the left column to the
##right column.
##
##Paths can move up, down, and right, but not left.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

def solve():
        startTime = time() #oops i screwed it up
        #Get matrix into a text file
        chdir("textfiles")
        file = open("p082_matrix.txt")
        rawmatrix = []
        for line in file:
                rawmatrix.append(line.split(','))
        for row in range(len(rawmatrix)):
                for col in range(len(rawmatrix[row])):
                        rawmatrix[row][col] = int(rawmatrix[row][col])
        #Rotate the matrix to switch rows and columns
        matrix = []
        for coltorow in range(len(rawmatrix)):
                matrix.append([])
                for rowtocol in range(len(rawmatrix[0])):
                        matrix[coltorow].append(rawmatrix[rowtocol][coltorow])
        #Solve for each row in turn
        for row in range(len(matrix) - 2, -1, -1):
                editedrow = []
                for start in range(len(matrix[row])):
                        #Case 1: Smallest is straight down
                        smallest = matrix[row][start] + matrix[row + 1][start]
                        #Case 2: Smallest is left, then down
                        for leftstop in range(start):
                                pathsum = sum(matrix[row][leftstop:start + 1])
                                pathsum += matrix[row + 1][leftstop]
                                if pathsum < smallest:
                                        smallest = pathsum
                        #Case 3: Smallest is right, then down
                        for rightstop in range(start + 1, len(matrix[row])):
                                pathsum = sum(matrix[row][start:rightstop + 1])
                                pathsum += matrix[row + 1][rightstop]
                                if pathsum < smallest:
                                        smallest = pathsum
                        editedrow.append(smallest)
                matrix[row] = editedrow
        result = min(matrix[0])
        peresult(82, result, time() - startTime)

if __name__ == "__main__":
        solve()
