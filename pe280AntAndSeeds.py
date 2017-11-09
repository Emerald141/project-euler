##A laborious ant walks randomly on a 5x5 grid. The walk starts from the central
##square. At each step, the ant moves to an adjacent square at random, without
##leaving the grid; thus there are 2, 3 or 4 possible moves at each step
##depending on the ant's position.
##
##At the start of the walk, a seed is placed on each square of the lower row.
##When the ant isn't carrying a seed and reaches a square of the lower row
##containing a seed, it will start to carry the seed. The ant will drop the
##seed on the first empty square of the upper row it eventually reaches.
##
##What's the expected number of steps until all seeds have been dropped in
##the top row?
##Give your answer rounded to 6 decimal places.

from time import time
from peresult import peresult
from matrixfns import solve, show

def toBin(theseSeedBools):
    binary = 0
    for x in range(len(theseSeedBools)):
        binary += (2 ** x) * theseSeedBools[x]
    return binary

def pe280():
    #Stage 0: All seeds on bottom
    #Stage 1: 4 bottom
    #Stage 2: 4 bottom, 1 top
    #Stage 3: 3 bottom, 1 top
    #Stage 4: 3 bottom, 2 top
    #...
    #Stage 9: 0 bottom, 4 top
    #Stage 10: All seeds on top
    #Bottom rows represented by 2**0, 2**1, 2**2, 2**3, 2**4
    #Top rows represented by 2**5, 2**6, 2**7, 2**8, 2**9
    start = time()
    #Expected number of steps remaining at position in layout
    startRows = [ [0, 0, 0, 0, 0] for x in range(2**10)]
    #Synthetic nested for loops to hit all combos
    seedBools = [0 for x in range(10)] #Is a seed at the given position?
    stages = [ [] for x in range(11)]
    while True:
        if seedBools[-1] == 0:
            seedBools[-1] = 1
        else:
            pointer = len(seedBools) - 1
            while seedBools[pointer] == 1 and pointer >= 0:
                seedBools[pointer] = 0
                pointer -= 1
            if pointer == -1:
                break
            seedBools[pointer] = 1
        if sum(seedBools) == 5: #Even-numbered stages
            stages[sum(seedBools[5:]) * 2].append(seedBools[:])
        elif sum(seedBools) == 4: #Odd-numbered stages
            stages[(sum(seedBools[5:]) * 2) + 1].append(seedBools[:])
    #That might have taken longer than just typing ten for loops. Oops.
    for stageNum in range(9, -1, -1): #Last stage stays at 0
        for layout in stages[stageNum]:
            #Set up the mutual dependency matrix
            matrix = [ [0 for col in range(26)] for row in range(25)]
            for row in range(len(matrix)):
                matrix[row][row] = 1
                matrix[row][25] = 1
            #Corners
            matrix[0][1], matrix[0][5] = -1/2, -1/2
            matrix[4][3], matrix[4][9] = -1/2, -1/2
            matrix[20][15], matrix[20][21] = -1/2, -1/2
            matrix[24][19], matrix[24][23] = -1/2, -1/2
            #Top edge
            for entry in range(1, 4):
                matrix[entry][entry-1] = -1/3
                matrix[entry][entry+1] = -1/3
                matrix[entry][entry+5] = -1/3
            #Left edge
            for entry in range(5, 16, 5):
                matrix[entry][entry-5] = -1/3
                matrix[entry][entry+1] = -1/3
                matrix[entry][entry+5] = -1/3
            #Right edge
            for entry in range(9, 20, 5):
                matrix[entry][entry-5] = -1/3
                matrix[entry][entry-1] = -1/3
                matrix[entry][entry+5] = -1/3
            #Bottom edge
            for entry in range(21, 24):
                matrix[entry][entry-5] = -1/3
                matrix[entry][entry-1] = -1/3
                matrix[entry][entry+1] = -1/3
            #Middle entries
            for row in range(5, 16, 5):
                for col in range(1, 4):
                    matrix[row+col][row+col-5] = -1/4
                    matrix[row+col][row+col-1] = -1/4
                    matrix[row+col][row+col+1] = -1/4
                    matrix[row+col][row+col+5] = -1/4
            #If the ant is carrying a seed and gets to an empty top square
            if stageNum % 2 == 1:
                for entry in range(5):
                    if layout[entry + 5] == 0:
                        matrix[entry] = [0 for x in range(26)]
                        matrix[entry][entry] = 1
                        matrix[entry][25] = \
                            startRows[toBin(layout) + 2**(entry + 5)][entry]
            #If the ant isn't carring a seed and gets to a full bottom square
            if stageNum % 2 == 0:
                for entry in range(5):
                    if layout[entry] == 1:
                        matrix[entry + 20] = [0 for x in range(26)]
                        matrix[entry + 20][entry + 20] = 1
                        matrix[entry + 20][25] = \
                            startRows[toBin(layout) - 2**entry][entry]
            #Damn that took a lot of lines to set up
            solve(matrix)
            if stageNum == 0:
                result = matrix[12][25]
                break
            if stageNum % 2 == 0: #Store the values from the top
                startRows[toBin(layout)] = [matrix[i][25] for i in range(5)]
            else: #Store the values from the bottom
                startRows[toBin(layout)] = [matrix[i+20][25] for i in range(5)]
    result *= 10 ** 6
    result = round(result)
    result /= 10**6
    peresult(280, result, time() - start)

if __name__ == "__main__":
    pe280()
