# Consider a configuration of 64 triangles, organized in a larger triangle
# with eight smaller triangles to a side.
# 
# We wish to colour the interior of each triangle with one of three colours:
# red, green or blue, so that no two neighbouring triangles have the same
# colour. Such a colouring shall be called valid. Here, two triangles are
# said to be neighbouring if they share an edge.
# Note: if they only share a vertex, then they are not neighbours.
# 
# A colouring C' which is obtained from a colouring C by rotation or
# reflection is considered distinct from C unless the two are identical.
# 
# How many distinct valid colourings are there for the configuration?

# THEORY:
# 
# The trick is to start at the middle and work outwards.
# Divide the large triangle into four equal-sized 'blocks'.
# For each of the 3^4=81 possible edges of the middle block, count the number
# of colourings of a block which can border it.
# Then, for each of the 3^10=59049 colourings of the downward-pointing
# triangles in the middle block: Calculate the number of ways to fill in 
# the six upward-pointing triangles in that block, fetch the number of ways to
# colour in the other three blocks, and multiply.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import product

def config_to_hash(config):
    return sum([config[i] * 3 ** i for i in range(len(config))])

def solve():
    # Part 1: use dynamic programming to determine the number of possible
    # colourings of a corner block, given the colouring of the bordering
    # edge of the centre block
    down = [2, 2, 2]
    for degree in range(2,5):
        up = [0 for x in range(3 ** degree)]
        for up_config in product(range(3), repeat=degree):
            for down_config in product(range(3), repeat=degree - 1):
                # Are these two configs compatible?
                for i in range(degree - 1):
                    if down_config[i] in up_config[i:i+2]:
                        break
                else:
                    up_hash = config_to_hash(up_config)
                    down_hash = config_to_hash(down_config)
                    up[up_hash] += down[down_hash]
        down = [0 for x in range(3 ** degree)]
        for down_config in product(range(3), repeat=degree):
            for up_config in product(range(3), repeat=degree):
                # Are these two configs compatible?
                for i in range(degree):
                    if up_config[i] == down_config[i]:
                        break
                else:
                    up_hash = config_to_hash(up_config)
                    down_hash = config_to_hash(down_config)
                    down[down_hash] += up[up_hash]
    # Now "down" is the list of borders.
    # Part 2: cycle through all 3^10 colourings of the down-triangles
    # in the centre.
    result = 0
    for centre in product(range(3), repeat=10):
        term = 1
        for tri in ((0, 1, 4), (1, 2, 5), (2, 3, 6), \
                    (4, 5, 7), (5, 6, 8), (7, 8, 9)):
            colors = set(centre[tri[i]] for i in range(3))
            term *= [2, 1, 0][len(colors) - 1]
        for edge in ((0, 1, 2, 3), (0, 4, 7, 9), (3, 6, 8, 9)):
            config = [centre[edge[i]] for i in range(4)]
            term *= down[config_to_hash(config)]
        result += term
    return result

if __name__ == "__main__":
    start = time()
    peresult(189, solve(), time() - start)
