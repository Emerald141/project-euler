# An ant moves on a regular grid of squares that are coloured
# either black or white.
# The ant is always oriented in one of the cardinal directions
# (left, right, up or down) and moves from square to adjacent square
# according to the following rules:
# - if it is on a black square, it flips the color of the square to white,
# rotates 90 degrees counterclockwise and moves forward one square.
# - if it is on a white square, it flips the color of the square to black,
# rotates 90 degrees clockwise and moves forward one square.
# 
# Starting with a grid that is entirely white, how many squares are black
# after 1018 moves of the ant?

# THEORY:
#
# langtonant.com reveals that around the 10,000th step, the ant
# falls into a pattern of 104 steps that constructs an infinite highway,
# which turns 12 squares black per iteration. If we find the black square
# count at the beginning of some iteration, we can determine the black
# square count at an arbitrarily large number of steps.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap = 10 ** 18):
    start = time()
    # False means white, True means black
    grid_size = 100     # Simulation on langtonant.com shows this is large
                        # enough to contain the pre-highway chaos
    grid = [ [False for x in range(grid_size)] for y in range(grid_size)]
    blacks = 0      # The number of black tiles
    ant_position = [50, 50]
    ant_direction = 0   # 0 = up, 1 = right, 2 = down, 3 = left
    for step in range(10400 + (cap % 104)):     # Loose bound on chaos
        if grid[ant_position[0]][ant_position[1]]:  # On black tile
            ant_direction = (ant_direction - 1) % 4     # Turn counterclockwise
            grid[ant_position[0]][ant_position[1]] = False  # Flip color
            blacks -= 1
        else:
            ant_direction = (ant_direction + 1) % 4     # Turn clockwise
            grid[ant_position[0]][ant_position[1]] = True   # Flip color
            blacks += 1
        # Move the ant according to its new direction
        if ant_direction == 0:
            ant_position[1] -= 1
        elif ant_direction == 1:
            ant_position[0] += 1
        elif ant_direction == 2:
            ant_position[1] += 1
        else:
            ant_position[0] -= 1
    iterations = (cap - (cap % 104) - 10400) // 104
    result = blacks + (iterations * 12)     # 12 black squares per iteration
    peresult(349, result, time() - start)
    
if __name__ == "__main__":
    solve()
