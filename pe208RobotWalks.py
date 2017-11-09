##A robot moves in a series of one-fifth circular arcs (72°), with a free
##choice of a clockwise or an anticlockwise arc for each step, but no
##turning on the spot.
##
##Given that the robot starts facing North, how many journeys of 70 arcs
##in length can it take that return it, after the final arc, to its
##starting position?
##(Any arc may be traversed multiple times.)

from time import time
from peresult import peresult

def pe208():
    start = time()
    sums = [ [] for x in range(76)]
    for dc0 in range(15): #Segment count for direction 0
        for dc1 in range(15):
            for dc2 in range(15):
                for dc3 in range(15):
                    for dc4 in range(15):
                        sums[dc0 + dc1 + dc2 + dc3 + dc4].append( \
                            (dc0, dc1, dc2, dc3, dc4) )
    pathCounts = [[0 for direction in range(10)] for pathID in range(15**5)]
    #0: Traveling in direction 0, just turned left  (can go to 2 or 1 next)
    #1: Traveling in direction 0, just turned right (can go to 9 or 0 next)
    #2: Traveling in direction 1, just turned left  (can go to 4 or 3 next)
    #3: Traveling in direction 1, just turned right (can go to 1 or 2 next)
    #...
    #9: Traveling in direction 4, just turned right (can go to 7 or 8 next)
    #Direction 0 = just left of vertical, all others follow counterclockwise
    #All full paths consist of 14 segments in each direction
    pathCounts[0][1] = 1 #Initial condition
    for pathLengthCount in sums: #Iterates through all with sums of 0, then 1...
        for pathLengths in pathLengthCount:
            #Compute the hash
            pathID = 0
            for i in range(5):
                pathID += (15 ** i) * pathLengths[i]
            #print(pathLengths, pathID, pathCounts[pathID], sep='\t')
            for oldDir in range(5):
                #Continued rotations counterclockwise
                newDir = (oldDir + 1) % 5
                if pathLengths[newDir] < 14:
                    pathCounts[pathID + (15 ** newDir)][2 * newDir] \
                        += pathCounts[pathID][2 * oldDir]
                #Continued rotations clockwise
                newDir = (oldDir - 1) % 5
                if pathLengths[newDir] < 14:
                    pathCounts[pathID + (15 ** newDir)][(2 * newDir + 1) % 10] \
                        += pathCounts[pathID][(2 * oldDir + 1) % 10]
                #Proceeding along same direction as immediately previous
                if pathLengths[oldDir] < 14:
                    #Switching from left to right
                    pathCounts[pathID + (15 ** oldDir)][2 * oldDir + 1] \
                        += pathCounts[pathID][2 * oldDir]
                    #Switching from right to left
                    pathCounts[pathID + (15 ** oldDir)][2 * oldDir] \
                        += pathCounts[pathID][2 * oldDir + 1]
    result = sum(pathCounts[-1])
    peresult(208, result, time() - start)

if __name__ == "__main__":
    pe208()

