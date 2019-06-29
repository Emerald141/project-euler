# A series of three rooms are connected to each other by automatic doors.
#
# Each door is operated by a security card. Once you enter a room the door
# automatically closes and that security card cannot be used again. A machine
# at the start will dispense an unlimited number of cards, but each room
# (including the starting room) contains scanners and if they detect that you
# are holding more than three security cards or if they detect an unattended
# security card on the floor, then all the doors will become permanently locked.
# However, each room contains a box where you may safely store any number of
# security cards for use at a later stage.
#
# If you simply tried to travel through the rooms one at a time then as you
# entered room 3 you would have used all three cards and would be trapped in
# that room forever!
#
# However, if you make use of the storage boxes, then escape is possible. For
# example, you could enter room 1 using your first card, place one card in the
# storage box, and use your third card to exit the room back to the start. Then
# after collecting three more cards from the dispensing machine you could use
# one to enter room 1 and collect the card you placed in the box a moment ago.
# You now have three cards again and will be able to travel through the
# remaining three doors. This method allows you to travel through all three
# rooms using six security cards in total.
#
# It is possible to travel through six rooms using a total of 123 security
# cards while carrying a maximum of 3 cards.
#
# Let C be the maximum number of cards which can be carried at any time.
#
# Let R be the number of rooms to travel through.
#
# Let M(C,R) be the minimum number of cards required from the dispensing
# machine to travel through R rooms carrying up to a maximum of C cards at
# any time.
#
# For example, M(3,6)=123 and M(4,6)=23.
# And, ΣM(C,6)=146 for 3 ≤ C ≤ 4.
#
# You are given that ΣM(C,10)=10382 for 3 ≤ C ≤ 10.
#
# Find ΣM(C,30) for 3 ≤ C ≤ 40.

# THEORY:
#
# It helps to think of moving backwards in time.
# Right before the final shot to the finish, there will be a single keycard
# in each of the first R-C+1 rooms.
# Say at every stage, we know what the config of stored keys should be next.
# If we can't fill that config with a single trip out-and-back from the start,
# we should add as many keys to it as we can, as far out as we can.
# If the farthest out we need to fill is in room X, then we'll spend 2X keys
# on doors in the round trip, so the net loss of keys will be 2X-C.
# Any keys we have to subtract will be in the first few rooms, with at most
# two per room per trip, picked up upon entering and leaving that room.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(min_c = 3, max_c = 40, r = 30):
    result = 0
    for c in range(min_c, max_c + 1):
        if c > r:
            result += r + 1
            continue
        keys = [1 for x in range(r - c + 1)]
        result += c
        while sum(keys) > c - 2 * len(keys):
            change = [0 for x in range(len(keys))]
            l_ind, r_ind = 0, len(keys) - 1
            net = 2 * len(change) - c
            while sum(change) < net:
                change[l_ind] += 1
                if change[l_ind] == 2:
                    l_ind += 1
            while net < sum(change):
                change[r_ind] -= 1
                if change[r_ind] == -1 * min(c - 2, keys[r_ind]):
                    r_ind -= 1
            while l_ind < r_ind:
                change[l_ind] += 1
                if change[l_ind] == 2:
                    l_ind += 1
                change[r_ind] -= 1
                if -change[r_ind] == min(c - 2, keys[r_ind]):
                    r_ind -= 1
            repeat = (keys[-1] // (-change[-1]))
            for i in range(len(keys)):
                keys[i] += repeat * change[i]
            while len(keys) and keys[-1] == 0:
                del keys[-1]
            result += c * repeat
        if sum(keys):
            result += sum(keys) + 2 * len(keys)
    return result

if __name__ == "__main__":
    start = time()
    peresult(327, solve(), time() - start)
