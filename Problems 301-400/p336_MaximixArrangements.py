# A train is used to transport four carriages in the order: ABCD. However,
# sometimes when the train arrives to collect the carriages they are not in
# the correct order.
# To rearrange the carriages they are all shunted on to a large rotating
# turntable. After the carriages are uncoupled at a specific point the train
# moves off the turntable pulling the carriages still attached with it. The
# remaining carriages are rotated 180 degrees. All of the carriages are then
# rejoined and this process is repeated as often as necessary in order to
# obtain the least number of uses of the turntable.
# Some arrangements, such as ADCB, can be solved easily: the carriages are
# separated between A and D, and after DCB are rotated the correct order has
# been achieved.
#
# However, Simple Simon, the train driver, is not known for his efficiency,
# so he always solves the problem by initially getting carriage A in the
# correct place, then carriage B, and so on.
#
# Using four carriages, the worst possible arrangements for Simon, which
# we shall call maximix arrangements, are DACB and DBAC; each requiring him
# five rotations (although, using the most efficient approach, they could be
# solved using just three rotations). The process he uses for DACB is shown below.
#
#  D|A C B
# |D B C A
#  A C|B D
#  A|C D B
#  A B|D C
#  A B C D
#
# It can be verified that there are 24 maximix arrangements for six carriages,
# of which the tenth lexicographic maximix arrangement is DFAECB.
#
# Find the 2011th lexicographic maximix arrangement for eleven carriages.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import permutations

def reverse(string):
    return string[::-1]

def solve(carriage_count = 11, maximix_target = 2011):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    carriages = letters[:carriage_count]
    max_rotations = carriage_count * 2 - 3  # Rotations in a maximix arrangement
    rotations = {letters[:carriage_count]: 0}  # Stores already-computed counts
    maximix_count = 0
    def get_rotations(arrangement):
        if arrangement in rotations:
            return rotations[arrangement]
        for index in range(len(arrangement)):
            if arrangement[index] != letters[index]:
                if arrangement[-1] == letters[index]:  # if letter is at end
                    rotation_index = index
                else:
                    rotation_index = arrangement.index(letters[index])
                result = get_rotations(arrangement[:rotation_index] + \
                            reverse(arrangement[rotation_index:])) + 1
                rotations[arrangement] = result
                return result
    for arrangement_raw in permutations(carriages):  # gets them alphabetically
        arrangement = ''.join(arrangement_raw)
        if get_rotations(arrangement) == max_rotations:
            maximix_count += 1
            if maximix_count == maximix_target:
                return arrangement
    print("Error: Maximix target too high")

if __name__ == "__main__":
    start = time()
    peresult(336, solve(), time() - start)
