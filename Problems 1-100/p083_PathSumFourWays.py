# Find the minimal path sum, in matrix.txt, a 31K text file containing
# an 80 by 80 matrix, from the top left to the bottom right by moving
# left, right, up, and down.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

def solve():
    start = time()
    infinity = 9999999999999999999 #Close enough
    chdir("textfiles")
    file = open("pe82matrix.txt")
    matrix = []
    for x in range(80):
        matrix.append(file.readline().rstrip().split(','))
    for row in range(80):
        for col in range(80):
            matrix[row][col] = int(matrix[row][col])
    pathCost = [ [infinity for col in range(80)] for row in range(80)]
    pathCost[0][0] = matrix[0][0]
    visited = [ [False for col in range(80)] for row in range(80)]
    row, col = 0, 0 #Coordinates of square currently being visited
    while row != 79 or col != 79:
        visited[row][col] = True
        if row > 0: #not in top row
            if pathCost[row][col] + matrix[row-1][col] < pathCost[row-1][col]:
                pathCost[row-1][col] = pathCost[row][col] + matrix[row-1][col]
        if col > 0: #not in left column
            if pathCost[row][col] + matrix[row][col-1] < pathCost[row][col-1]:
                pathCost[row][col-1] = pathCost[row][col] + matrix[row][col-1]
        if row < 79: #not in bottom row
            if pathCost[row][col] + matrix[row+1][col] < pathCost[row+1][col]:
                pathCost[row+1][col] = pathCost[row][col] + matrix[row+1][col]
        if col < 79: #not in right column
            if pathCost[row][col] + matrix[row][col+1] < pathCost[row][col+1]:
                pathCost[row][col+1] = pathCost[row][col] + matrix[row][col+1]
        minCost = infinity
        minRow, minCol = 0, 0
        for rowN in range(80):
            for colN in range(80):
                if not visited[rowN][colN] and pathCost[rowN][colN] < minCost:
                    minCost = pathCost[rowN][colN]
                    minRow, minCol = rowN, colN
        row = minRow
        col = minCol
    peresult(83, pathCost[79][79], time() - start)

if __name__ == "__main__":
    solve()
