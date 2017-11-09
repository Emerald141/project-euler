##Work out the first ten digits of the sum of
##the following one-hundred 50-digit numbers.

from time import time
from peresult import peresult
from os import chdir

def pe13():
        start = time()
        chdir("textfiles")
        file = open('pe13longnums.txt')
        nums = []
        for line in file:
                if line[-1] == '\n':
                        nums.append(int(line[:-1]))
                else:
                        nums.append(int(line))
        longnum = sum(nums)
        while longnum >= 10 ** 10:
                longnum //= 10
        peresult(13, longnum, time() - start)
        
if __name__ == "__main__":
        pe13()
