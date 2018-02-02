##Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
##and each line adding to nine.
##
##(picture of a filled 3-gon because i can't past pics into Python)
##
##Working clockwise, and starting from the group of three with the
##numerically lowest external node (4,3,2 in this example), each solution
##can be described uniquely. For example, the above solution can be described
##by the set: 4,3,2; 6,2,1; 5,1,3.
##
##It is possible to complete the ring with four different totals: 9, 10, 11,
##and 12. There are eight solutions in total.
##
##Total	Solution Set
##9	4,2,3; 5,3,1; 6,1,2
##9	4,3,2; 6,2,1; 5,1,3
##10	2,3,5; 4,5,1; 6,1,3
##10	2,5,3; 6,3,1; 4,1,5
##11	1,4,6; 3,6,2; 5,2,4
##11	1,6,4; 5,4,2; 3,2,6
##12	1,5,6; 2,6,4; 3,4,5
##12	1,6,5; 3,5,4; 2,4,6
##
##By concatenating each group it is possible to form 9-digit strings; the
##maximum string for a 3-gon ring is 432621513.
##
##Using the numbers 1 to 10, and depending on arrangements, it is possible
##to form 16- and 17-digit strings. What is the maximum *16-digit* string
##for a "magic" 5-gon ring?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    #Represent four of the outer nodes and two linear inner nodes
    #The inner nodes are in line with the first outer node
    values = [10, 10, 10, 10, 9, 9]
    valuesMax = [10, 10, 10, 10, 9, 9]
    largest = 0
    finished = False
    while True:
        #Advance the synthetic nested for loops
        if values[-1] != 1:
            values[-1] -= 1
        else:
            pointer = len(values) - 1
            while values[pointer] == 1:
                values[pointer] = valuesMax[pointer]
                pointer -= 1
                if pointer == -1:
                    finished = True
                    break
            if finished: break            
            values[pointer] -= 1
        valuesFull = values + [values[0] + values[4] - values[1], \
                               values[1] + values[5] - values[2], \
                               values[0] - values[1] + values[2]  \
                                   - values[3] + values[4],       \
                               values[1] - values[2] + values[3]  \
                                   - values[4] + values[5] ]
        if len(set(valuesFull)) == 10 and valuesFull[6] in range(1, 10) \
           and valuesFull[7] in range(1, 10) and valuesFull[8] in range(1, 10) \
           and valuesFull[9] in range(1, 11) \
           and values[0] < min(values[1], values[2], values[3], valuesFull[9]):
            v = valuesFull #Makes it easier to type
            numstring = str(v[0]) + str(v[4]) + str(v[5])
            numstring += str(v[1]) + str(v[5]) + str(v[6])
            numstring += str(v[2]) + str(v[6]) + str(v[7])
            numstring += str(v[3]) + str(v[7]) + str(v[8])
            numstring += str(v[9]) + str(v[8]) + str(v[4])
            largest = max(largest, int(numstring))
    peresult(68, largest, time() - start)

if __name__ == "__main__":
    solve()
