##"The Chase" is a game played with two dice and an even number of players.
##
##The players sit around a table; the game begins with two opposite players
##having one die each. On each turn, the two players with a die roll it.
##If a player rolls a 1, he passes the die to his neighbour on the left;
##if he rolls a 6, he passes the die to his neighbour on the right;
##otherwise, he keeps the die for the next turn.
##The game ends when one player has both dice after they have been rolled
##and passed; that player has then lost.
##
##In a game with 100 players, what is the expected number of turns
##the game lasts?
##
##Give your answer rounded to ten significant digits.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    
    matrix = [ [0 for x in range(52)] for x in range(51)]

    #Case for when d = 0
    matrix[0][0] = 1

    #Case for when d = 1
    matrix[1][1] = 1
    matrix[1][2] = -8/17
    matrix[1][3] = -1/17
    matrix[1][51] = 36/17

    #Case for when 2 <= d <= 48
    for d in range(2, 49):
        matrix[d][d-2] = -1/18
        matrix[d][d-1] = -4/9
        matrix[d][d] = 1
        matrix[d][d+1] = -4/9
        matrix[d][d+2] = -1/18
        matrix[d][51] = 2
            
    #Case for when d = 49
    matrix[49][47] = -1/17
    matrix[49][48] = -8/17
    matrix[49][49] = 1
    matrix[49][50] = -8/17
    matrix[49][51] = 36/17

    #Case for when d = 50
    matrix[50][48] = -1/9
    matrix[50][49] = -8/9
    matrix[50][50] = 1
    matrix[50][51] = 2

    rref(matrix)
    
    result = matrix[-1][-1]
    powers = 0
    while result < 10**9:
        result *= 10
        powers += 1
    result = int(result + .5)
    result /= 10 ** powers
    
    peresult(227, result, time() - start)

#NOTE:
#The following is imported from the "matrixsolver" program in the main
#Python34 folder. Yeah, it's pretty ugly, I know. But it works.

def rref(matrix, printing=False): #Assuming nonempty input
    height = len(matrix)
    width = len(matrix[0])
    toprow = 0
    leftcol = 0
    if printing:
        show(matrix)
    while True:
        #Step 1: Find first column that isn't all 0's
        pivotrow, pivotcol = -1, -1
        for col in range(leftcol, width):
            for row in range(toprow, height):
                if matrix[row][col] != 0:
                    pivotrow, pivotcol = row, col
                    break
            else:
                continue
            break
        if pivotrow == -1: break #all done
        #If pivot is not in top row, move it there
        if pivotrow != toprow:
            matrix[pivotrow], matrix[toprow] = matrix[toprow], matrix[pivotrow]
            if printing:
                print("Swap R", pivotrow + 1, " and R", toprow + 1, sep='')
                show(matrix)
        #Step 2: Divide first row by pivot
        divisor = matrix[toprow][pivotcol]
        for col in range(width):
            matrix[toprow][col] /= divisor
        if printing:
            print("R", toprow + 1, " / ", snip(divisor), sep='')
            show(matrix)
        #Step 3: Add multiples of pivot row to other rows
        for row in range(height):
            if row == toprow:
                continue
            multiplier = -1 * matrix[row][pivotcol]
            for col in range(pivotcol, width):
                matrix[row][col] += multiplier * matrix[toprow][col]
            if printing:
                print("R", row + 1, " + ", snip(multiplier), " R", toprow + 1, sep='')
        #Step 4: Repeat
        if printing:
            show(matrix)
        toprow += 1
        leftcol = pivotcol + 1
    return matrix

def show(matrix):
    for row in matrix:
        for entry in row:
            print(snip(entry), end = '\t')
        print()
    print()

def snip(decimal):
    output = decimal * 1000 // 1 / 1000
    if output % 1 == 0:
        return int(output)
    return output

if __name__ == "__main__":
    solve()
