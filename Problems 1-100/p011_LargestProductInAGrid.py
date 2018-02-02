# What is the greatest product of four adjacent numbers in
# the same direction (up, down, left, right, or diagonally)
# in the 20×20 grid?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

def solve():
    chdir("../textfiles")
    file = open('p011_grid.txt')
    grid = []
    for row in range(20):
        rawstring = file.readline()
        grid.append([])
        for col in range(20):
            grid[row].append(int(rawstring[col * 3:col * 3 + 2]))
    largest = 0
    #From left going right:
    for r in range(20):
        for c in range(17):
            product = 1
            for offset in range(4):
                product *= grid[r][c+offset]
            if product > largest:
                largest = product
    #From top going down:
    for r in range(17):
        for c in range(20):
            product = 1
            for offset in range(4):
                product *= grid[r+offset][c]
            if product > largest:
                largest = product
    #From top-left going down-right:
    for r in range(17):
        for c in range(17):
            product = 1
            for offset in range(4):
                product *= grid[r+offset][c+offset]
            if product > largest:
                largest = product
    #From top-right going down-left:
    for r in range(17):
        for c in range(3, 20):
            product = 1
            for offset in range(4):
                product *= grid[r+offset][c-offset]
            if product > largest:
                largest = product
    return largest

if __name__ == "__main__":
    start = time()
    peresult(11, solve(), time() - start)
