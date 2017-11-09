##Let T(n) be the number of tours over a 4 × n playing board such that:
##
##The tour starts in the top left corner.
##The tour consists of moves that are up, down, left, or right one square.
##The tour visits each square exactly once.
##The tour ends in the bottom left corner.
##
##T(10) is 2329. What is T(10 ** 12) modulo 10 ** 8?

##This piece of code follows a fairly complex thought process which
##would be just about impossible to explain to somebody else, and
##which I myself might have a hard time understanding should I
##return here later for whatever reason.
##
##Basically it involves listing the markings in each possible column,
##then running a simulation to see how many gridpaths can end with
##that particular column path. Some of these column paths will always
##have the same number of possibilities as some others, so those are
##grouped together in the algorithm.
##
##By using the results for 10 * (x-1) steps for a given set of these
##tiles, it is possible to find the results for 10 * x steps in those
##same tiles.
##
##A low-quality picture of my notes can be found at
##http://i.imgur.com/PCHCdgn.jpg
##This may or may not be helpful in attempting to decipher how I
##got to the conclusion I did.

from time import time
from peresult import peresult

def pe237():
        start = time()
        laststep = []
        for x in range(5):
                tiles = [0 for y in range(5)]
                tiles[x] = 1
                laststep.append(tileround(tiles, 10))
        for nextpower in range(11):
                newstep = []
                for x in range(5):
                        tiles = laststep[x]
                        for tenmult in range(9):
                                newtiles = [0, 0, 0, 0, 0]
                                for entry in range(5):
                                        mat = [tiles[entry] * laststep[entry][i] % (10 ** 15) for i in range(len(laststep[0]))]
                                        newtiles = matrixadd(newtiles, mat)
                                tiles = newtiles
                        newstep.append(tiles)
                laststep = newstep
        result = laststep[0][2] % (10 ** 8)
        peresult(237, result, time() - start)
        
def matrixadd(*mats):
	result = mats[0]
	for index in range(len(mats[0])):
		for mat in range(1, len(mats)):
			result[index] += mats[mat][index]
	return result

def tileround(tiles, num):
        #Returns values of A, B, C, D, and E after num cols added to col 1.
        #So, for example, tileround([1,0,0,0,0], 10) would be for a 4x11 board.
	for turn in range(num):
		newtiles = [0 for x in range(5)]
		newtiles[0] = tiles[1] + 2 * tiles[2] + tiles[3]
		newtiles[1] = tiles[0]
		newtiles[2] = tiles[0] + tiles[2]
		newtiles[3] = 2 * (tiles[2] + tiles[4])
		newtiles[4] = tiles[2] + tiles[4]
		tiles = newtiles
	return tiles

if __name__ == "__main__":
        pe237()
