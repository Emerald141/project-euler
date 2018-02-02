# By starting at the top of the triangle below and
# moving to adjacent numbers on the row below, the
# maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the
# triangle in the textfiles folder.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    file = open("../textfiles/p018_triangle.txt")
    # Parse the triangle into a 2D array
    triangle = []
    for line in file:
        line = line.strip()  # Eliminates \n at end
        triangle.append([])
        for x in range(0, len(line), 3):
            triangle[-1].append(int(line[x:x+2]))
    # triangle[row][col] represents the most expensive way to get to the bottom
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            plus = max(triangle[row+1][col], triangle[row+1][col+1])
            triangle[row][col] += plus
    return triangle[0][0]

if __name__ == "__main__":
    start = time()
    peresult(18, solve(), time() - start)
