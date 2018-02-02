# Su Doku (Japanese meaning number place) is the name given to a popular puzzle
# concept. Its origin is unclear, but credit must be attributed to Leonhard
# Euler who invented a similar, and much more difficult, puzzle idea called
# Latin Squares. The objective of Su Doku puzzles, however, is to replace the
# blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3
# box contains each of the digits 1 to 9.
# 
# A well constructed Su Doku puzzle has a unique solution and can be solved by
# logic, although it may be necessary to employ "guess and test" methods in
# order to eliminate options (there is much contested opinion over this).
# The complexity of the search determines the difficulty of the puzzle; the
# example above is considered easy because it can be solved by straight forward
# direct deduction.
# 
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
# contains fifty different Su Doku puzzles ranging in difficulty, but all with
# unique solutions (the first puzzle in the file is the example above).
# 
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the
# top left corner of each solution grid; for example, 483 is the 3-digit number
# found in the top left corner of the solution grid above.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

#MODIFIED RULE: Entries are 0 to 8, not 1 to 9.
#An empty tile will temporarily be assigned a value of -1.

class Entry:
    def __init__(self):
        self.possibles = [True for x in range(9)]
        self.value = -1 #default

def solvePuzzle(lines):
    entriesLeft = 81
    grid = [ [Entry() for x in range(9)] for y in range(9)]
    def strikeFromPossibles(row, col, value):
        #Strike from the same row
        for otherCol in range(9):
            grid[row][otherCol].possibles[value] = False
        #Strike from the same col
        for otherRow in range(9):
            grid[otherRow][col].possibles[value] = False
        #Strike from the same box
        for otherRow in range(row // 3 * 3, row // 3 * 3 + 3):
            for otherCol in range(col // 3 * 3, col // 3 * 3 + 3):
                grid[otherRow][otherCol].possibles[value] = False
        #Strike all other values from THIS entry
        for otherValue in range(9):
            grid[row][col].possibles[otherValue] = False
    #Set up the grid
    for row in range(9):
        for col in range(9):
            presetValue = int(lines[row][col]) - 1
            if presetValue != -1:
                entriesLeft -= 1
                strikeFromPossibles(row, col, presetValue)
                grid[row][col].value = presetValue
    #Keep solving entries until puzzle is done
    while entriesLeft > 0:
        solvedTile = False #Has solved at least one tile this loop
        #Check tiles. Just one possibility?
        for row in range(9):
            for col in range(9):
                if grid[row][col].value == -1 \
                   and sum(grid[row][col].possibles) == 1:
                    entriesLeft -= 1
                    solvedTile = True
                    #Assign a value to this entry
                    determinedValue = -1
                    for index in range(9):
                        if grid[row][col].possibles[index]:
                            determinedValue = index
                    grid[row][col].value = determinedValue
                    #Update adjacent values
                    strikeFromPossibles(row, col, determinedValue)
        #Check rows. Just one spot for a number?
        for row in range(9):
            for testValue in range(9):
                goodCol = -1
                for col in range(9):
                    if grid[row][col].value == testValue:
                        break
                    if grid[row][col].possibles[testValue]:
                        if goodCol != -1:
                            break
                        goodCol = col
                else:
                    if goodCol != -1:
                        entriesLeft -= 1
                        solvedTile = True
                        grid[row][goodCol].value = testValue
                        strikeFromPossibles(row, goodCol, testValue)
        #Check cols. Just one spot for a number?
        for col in range(9):
            for testValue in range(9):
                goodRow = -1
                for row in range(9):
                    if grid[row][col].value == testValue:
                        break
                    if grid[row][col].possibles[testValue]:
                        if goodRow != -1:
                            break
                        goodRow = row
                else:
                    if goodRow != -1:
                        entriesLeft -= 1
                        solvedTile = True
                        grid[goodRow][col].value = testValue
                        strikeFromPossibles(goodRow, col, testValue)
        #Check boxes. Just one spot for a number?
        for baseRow in range(0, 7, 3):
            for baseCol in range(0, 7, 3):
                for testValue in range(9):
                    #print("In loop: baseRow =", baseRow, "baseCol =", baseCol, "testValue =", testValue)
                    canAppear = True
                    goodRow, goodCol = -1, -1
                    for row in range(baseRow, baseRow + 3):
                        for col in range(baseCol, baseCol + 3):
                            if grid[row][col].value == testValue:
                                canAppear = False
                                break
                            if grid[row][col].possibles[testValue]:
                                #print("Match: row =", row, "col =", col)
                                if goodRow != -1:
                                    canAppear = False
                                    break
                                goodRow, goodCol = row, col
                    if canAppear and goodRow != -1:
                        entriesLeft -= 1
                        solvedTile = True
                        grid[goodRow][goodCol].value = testValue
                        strikeFromPossibles(goodRow, goodCol, testValue)
        if not solvedTile: #none of these four methods work anymore
            output = [ [-1 for col in range(9)] for row in range(9)]
            for row in range(9):
                for col in range(9):
                    output[row][col] = grid[row][col].value
            return solveBacktrack(output)
    return (grid[0][0].value + 1) * 100 \
           + (grid[0][1].value + 1) * 10 \
           + (grid[0][2].value + 1)

def solveBacktrack(array):
    #Find the first unfilled tile
    row, col = -1, -1
    for r in range(9):
        for c in range(9):
            if array[r][c] == -1:
                row, col = r, c
                break
        else:
            continue
        break
    #If no unfilled tiles, return the puzzle's solution
    if row == -1:
        return (array[0][0] + 1) * 100 \
               + (array[0][1] + 1) * 10 \
               + (array[0][2] + 1)
    #For all possible values:
    for value in range(9):
        #Is the tile prevented from being the value...
        valueIsPossible = True
        #...by a tile in the same row?
        for otherCol in range(9):
            if array[row][otherCol] == value:
                valueIsPossible = False
                break
        #...by a tile in the same column?
        for otherRow in range(9):
            if array[otherRow][col] == value:
                valueIsPossible = False
                break
        #...by a tile in the same box?
        for otherRow in range(row // 3 * 3, row // 3 * 3 + 3):
            for otherCol in range(col // 3 * 3, col // 3 * 3 + 3):
                if array[otherRow][otherCol] == value:
                    valueIsPossible = False
                    break
            else:
                continue
            break
        #If so, try a different value
        if not valueIsPossible:
            continue
        #Create a new array with that value inserted
        newArray = array[:]
        newArray[row] = array[row][:]
        newArray[row][col] = value
        #Recursively call the function on this new array
        possibleSolution = solveBacktrack(newArray)
        #If it gives -1, try a new possible value
        if possibleSolution == -1:
            continue
        #If not, return the number it outputs (the puzzle's solution)
        else:
            return possibleSolution
    #If no possible values work, return -1; something went wrong earlier up
    return -1

def solve():
    start = time()
    chdir("textfiles")
    file = open("p096_sudoku.txt")
    result = 0
    for puzzleNumber in range(50):
        file.readline() #Skip the header
        lines = []
        for row in range(9):
            lines.append(file.readline())
        puzzleSolution = solvePuzzle(lines)
        result += puzzleSolution
    peresult(96, result, time() - start)

if __name__ == "__main__":
    solve()
