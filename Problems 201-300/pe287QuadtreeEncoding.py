##The quadtree encoding allows us to describe a 2N×2N black and
##white image as a sequence of bits (0 and 1). Those sequences are
##to be read from left to right like this:
##
##* the first bit deals with the complete 2N×2N region;
##* "0" denotes a split: 
##** the current 2n×2n region is divided into 4 sub-regions of
##dimension 2n-1×2n-1,
##** the next bits contains the description of the top left,
##top right, bottom left and bottom right sub-regions - in that order;
##* "10" indicates that the current region contains only black pixels;
##* "11" indicates that the current region contains only white pixels.
##
##For a positive integer N, define D(N) as the 2N×2N image with the
##following coloring scheme:
##
##* the pixel with coordinates x = 0, y = 0 corresponds to the bottom left pixel,
##* if (x - 2N-1)2 + (y - 2N-1)2 ≤ 22N-2 then the pixel is black,
##* otherwise the pixel is white.
##
##What is the length of the minimal sequence describing D(24)?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        print("Note: This one takes a while. I haven't found a way to optimize it into running under nine minutes, let alone one.")
        start = time()
        result = 5 + seqLength([2 ** 22, 2 ** 22]) + seqLength([0, 0]) + 2 * seqLength([2 ** 22, 0])
        result += 2 * seqLength([2 ** 23, 0]) + 2 * seqLength([2 ** 23, 2 ** 22]) + 2 * seqLength([2 ** 23 + 2 ** 22, 0]) + 2 * seqLength([2 ** 23 + 2 ** 22, 2 ** 22])
        result += seqLength([2 ** 23, 2 ** 23]) + 2 * seqLength([2 ** 23 + 2 ** 22, 2 ** 23]) + seqLength([2 ** 23 + 2 ** 22, 2 ** 23 + 2 ** 22])
        peresult(287, result, time() - start)

def isBlack(coord):
        return (coord[0] - 2 ** 23) ** 2 + (coord[1] - 2 ** 23) ** 2 <= 2 ** 46

def seqLength(initialCoord):
        startCoords = [initialCoord]
        result = 0
        for twopow in range(22, 0, -1):
                newStartCoords = []
                for startCoord in startCoords:
                        endCoord1 = [startCoord[0] + 2 ** twopow - 1, startCoord[1] + 2 ** twopow - 1]
                        endCoord2 = [startCoord[0], startCoord[1] + 2 ** twopow - 1]
                        endCoord3 = [startCoord[0] + 2 ** twopow - 1, startCoord[1]]
                        if isBlack(startCoord) == isBlack(endCoord1) == isBlack(endCoord2) == isBlack(endCoord3) :
                                result += 2
                        else:
                                result += 1
                                shift = 2 ** (twopow - 1)
                                newStart2 = [startCoord[0], startCoord[1] + shift]
                                newStart3 = [startCoord[0] + shift, startCoord[1] + shift]
                                newStart4 = [startCoord[0] + shift, startCoord[1]]
                                newStartCoords.extend([startCoord, newStart2, newStart3, newStart4])
                startCoords = newStartCoords
        result += 2 * len(startCoords)
        return result

if __name__ == "__main__":
        solve()
