# Work out the first ten digits of the sum of the one-hundred 50-digit
# stored in the text file.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

def solve():
    chdir("../textfiles")
    file = open('p013_longnums.txt')
    nums = []
    for line in file:
        if line[-1] == '\n':
            nums.append(int(line[:-1]))
        else:
            nums.append(int(line))
    result = sum(nums)
    while result >= 10 ** 10:
        result //= 10
    return result

if __name__ == "__main__":
    start = time()
    peresult(13, solve(), time() - start)
