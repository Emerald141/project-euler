##A row measuring seven units in length has red blocks with a minimum
##length of three units placed on it, such that any two red blocks
##(which are allowed to be different lengths) are separated by at least
##one black square. There are exactly seventeen ways of doing this.
##
##How many ways can a row measuring fifty units in length be filled?
##
##In general it is permitted to mix block sizes. For example, on a row
##eight units in length you could use red (3), black (1), and red (4).

from time import time
from peresult import peresult

def pe114(rowlength):
        start = time()
        result = 1 #counting the one with all black tiles
        assignments = [ [0 for x in range(14)] for y in range(51)] #assignments[squares][blocks]
        assignments[0] = [1 for x in range(14)]
        assignments[1] = [x for x in range(14)]
        for squares in range(2, len(assignments)):
                for blocks in range(1, len(assignments[squares])):
                        if blocks == 1:
                                assignments[squares][blocks] = 1
                                continue
                        for squaresFuture in range(squares + 1):
                                assignments[squares][blocks] += assignments[squaresFuture][blocks-1]
        for redSquares in range(3, rowlength + 1):
                redBlockMax = redSquares // 3
                while redSquares + redBlockMax - 1 > rowlength:
                        redBlockMax -= 1
                for redBlocks in range(1, redBlockMax + 1):
                        redFrees = redSquares - (3 * redBlocks)
                        blackFrees = rowlength - redSquares - redBlocks + 1
                        result += assignments[redFrees][redBlocks] * assignments[blackFrees][redBlocks + 1]
        peresult(114, result, time() - start)

if __name__ == "__main__":
        pe114(50)
