# Consider the problem of building a wall out of 2×1 and 3×1 bricks
# (horizontal×vertical dimensions) such that, for extra strength, the
# gaps between horizontally-adjacent bricks never line up in consecutive
# layers, i.e. never form a "running crack".
# 
# There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.
# 
# Calculate W(32,10).

# THEORY:
# 
# This problem can be solved by making an adjacency matrix of brick rows
# (that is, determining which rows can be on top of or below each other)
# and using dynamic programming from there.
# 
# If one row starts with a 3-brick, the second has to start with a 2-brick.
# Without loss of generality, say that the top row starts with a 3-brick.
# Then in the fourth column, the top row will have the first square of a brick
# and the bottom row will have the second square of a brick.
# The transition matrix for top-bottom pairs, going right, is
#   (1,2) -> (2,3) -> (3,1) -> (1,2)
#   ^ |
#   | v
#   (2,1) -> (3,2) -> (1,3) -> (2,1)
# The states which can end the wall are (2,3) and (3.2).
# There are 28 more steps, consisting of 3-cycles and single steps, the last
# of which must be a single step. So let's just say there are 27 more steps.
# 
# Going around each 3-loop, both top and bottom get a new 3-brick.
# Going from (1,2) to (2,1), the bottom gets a new 2-brick.
# Going from (2,1) to (1,2), the top gets a new 2-brick.
# 
# Each layer pair can be uniquely defined by how many 3-cycles there are, and
# how many single steps have been taken by the time each 3-cycle starts.
# Each row of bricks can be uniquely defined by how many 3-bricks there are,
# and how many 2-bricks precede each 3-brick.
# The latter can be deduced from the former if we know if it starts with a
# 3-brick or with a 2-brick.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import combinations_with_replacement as cwr

def solve():
    links = dict()
    for tri_count in range(10):
        for pair in cwr(range(28 - 3 * tri_count), tri_count):
            tup1 = ('t',) + tuple(map(lambda x: x // 2, pair))
            tup2 = ('b',) + tuple(map(lambda x: (x + 1) // 2, pair))
            if tup1 not in links: links[tup1] = []
            if tup2 not in links: links[tup2] = []
            links[tup1].append(tup2)
            links[tup2].append(tup1)
    configs = dict()
    for layer in links:
        configs[layer] = 1
    for new_row in range(9):
        new_configs = dict()
        for layer in links:
            for new_layer in links[layer]:
                if new_layer in new_configs:
                    new_configs[new_layer] += configs[layer]
                else:
                    new_configs[new_layer] = configs[layer]
        configs = new_configs
    result = 0
    for layer in configs:
        result += configs[layer]
    return result

if __name__ == "__main__":
    start = time()
    peresult(215, solve(), time() - start)
