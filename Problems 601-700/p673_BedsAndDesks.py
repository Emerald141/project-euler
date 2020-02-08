# At Euler University, each of the n students (numbered from 1 to n) occupies
# a bed in the dormitory and uses a desk in the classroom.
#
# Some of the beds are in private rooms which a student occupies alone, while
# the others are in double rooms occupied by two students as roommates.
# Similarly, each desk is either a single desk for the sole use of one student,
# or a twin desk at which two students sit together as desk partners.
#
# We represent the bed and desk sharing arrangements each by a list of pairs
# of student numbers. For example, with n=4, if (2,3) represents the bed
# pairing and (1,3)(2,4) the desk pairing, then students 2 and 3 are roommates
# while 1 and 4 have single rooms, and students 1 and 3 are desk partners, as
# are students 2 and 4.
#
# The new chancellor of the university decides to change the organisation of
# beds and desks: he will choose a permutation σ of the numbers 1,2,…,n and
# each student k will be given both the bed and the desk formerly occupied by
# student number σ(k).
#
# The students agree to this change, under the conditions that:
#
# Any two students currently sharing a room will still be roommates.
# Any two students currently sharing a desk will still be desk partners.
# In the example above, there are only two ways to satisfy these conditions:
# either take no action (σ is the identity permutation), or reverse the order
# of the students.
#
# With n=6, for the bed pairing (1,2)(3,4)(5,6) and the desk pairing
# (3,6)(4,5), there are 8 permutations which satisfy the conditions. One
# example is the mapping (1,2,3,4,5,6)↦(1,2,5,6,3,4).
#
# With n=36, if we have bed pairing:
# (2,13)(4,30)(5,27)(6,16)(10,18)(12,35)(14,19)(15,20)(17,26)(21,32)
# (22,33)(24,34)(25,28)
# and desk pairing
# (1,35)(2,22)(3,36)(4,28)(5,25)(7,18)(9,23)(13,19)(14,33)(15,34)
# (20,24)(26,29)(27,30)
# then among the 36! possible permutations (including the identity permutation),
# 663552 of them satisfy the conditions stipulated by the students.
#
# The downloadable text files beds.txt and desks.txt contain pairings for n=500.
# Each pairing is written on its own line, with the student numbers of the two
# roommates (or desk partners) separated with a comma. For example, the desk
# pairing in the n=4 example above would be represented in this file format as:
#
# 1,3
# 2,4
# With these pairings, find the number of permutations that satisfy the
# students' conditions. Give your answer modulo 999999937.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

start = time()

size = 500
mod = 999999937

bed_file = open("../textfiles/p673_beds.txt")
desk_file = open("../textfiles/p673_desks.txt")
bed_partner = [0 for x in range(size + 1)]
desk_partner = [0 for x in range(size + 1)]
for line in bed_file:
    pair = list(map(int, line.strip().split(',')))
    bed_partner[pair[0]] = pair[1]
    bed_partner[pair[1]] = pair[0]
for line in desk_file:
    pair = list(map(int, line.strip().split(',')))
    desk_partner[pair[0]] = pair[1]
    desk_partner[pair[1]] = pair[0]

# size = 36
# bed_pairs = [[2,13],[4,30],[5,27],[6,16],[10,18],[12,35],[14,19],[15,20],[17,26],[21,32],[22,33],[24,34],[25,28]]
# desk_pairs = [[1,35],[2,22],[3,36],[4,28],[5,25],[7,18],[9,23],[13,19],[14,33],[15,34],[20,24],[26,29],[27,30]]
# for pair in bed_pairs:
#     bed_partner[pair[0]] = pair[1]
#     bed_partner[pair[1]] = pair[0]
# for pair in desk_pairs:
#     desk_partner[pair[0]] = pair[1]
#     desk_partner[pair[1]] = pair[0]

# Keep track of how many of each chain we've seen.
loops = [0 for i in range(size + 1)]
b_longs = [0 for i in range(size + 1)]
d_longs = [0 for i in range(size + 1)]
skews = [0 for i in range(size + 1)]
alones = sum([bed_partner[i] + desk_partner[i] == 0 for i in range(1,size + 1)])

for start_kid in range(1, size + 1):
    if bed_partner[start_kid] != 0:  # if this student shares a bed
        # Start constructing a new chain.
        length = 1
        kid = start_kid
        while True:
            if kid == start_kid and length != 1:
                right_end = 'loop'
                length -= 1
                break
            if length % 2 == 1:
                if bed_partner[kid] == 0:
                    right_end = 'desk'
                    break
                kid = bed_partner[kid]
                bed_partner[bed_partner[kid]] = 0
                bed_partner[kid] = 0
                length += 1
            else:
                if desk_partner[kid] == 0:
                    right_end = 'bed'
                    break
                kid = desk_partner[kid]
                desk_partner[desk_partner[kid]] = 0
                desk_partner[kid] = 0
                length += 1
        if right_end == 'loop':
            loops[length] += 1
            continue
        left_length = 0
        kid = start_kid
        while True:
            if left_length % 2 == 1:
                if bed_partner[kid] == 0:
                    left_end = 'desk'
                    break
                kid = bed_partner[kid]
                bed_partner[bed_partner[kid]] = 0
                bed_partner[kid] = 0
                left_length += 1
            else:
                if desk_partner[kid] == 0:
                    left_end = 'bed'
                    break
                kid = desk_partner[kid]
                desk_partner[desk_partner[kid]] = 0
                desk_partner[kid] = 0
                left_length += 1
        if left_end == right_end == 'desk':
            d_longs[length + left_length] += 1
        elif left_end == right_end == 'bed':
            b_longs[length + left_length] += 1
        else:
            skews[length + left_length] += 1

for i in range(size + 1):
    if desk_partner[i] != 0:
        d_longs[2] += 1
        desk_partner[desk_partner[i]] = 0
        desk_partner[i] = 0

factorial = [1 for i in range(size + 1)]
for i in range(1, size + 1):
    factorial[i] = (factorial[i-1] * i) % mod

result = factorial[alones]
for i in range(size + 1):
    if loops[i] != 0:
        result *= factorial[loops[i]] * pow(i, loops[i], mod)
        result %= mod
for array in b_longs, d_longs:
    for i in range(size + 1):
        if array[i] != 0:
            result *= factorial[array[i]] * pow(2, array[i], mod)
            result %= mod
for i in range(size + 1):
    if skews[i] != 0:
        result *= factorial[skews[i]]
        result %= mod

peresult(673, result, time() - start)
