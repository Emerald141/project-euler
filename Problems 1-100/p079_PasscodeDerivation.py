# A common security method used for online banking is
# to ask the user for three random characters from a
# passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters;
# the expected reply would be: 317.
# 
# The text file, keylog.txt, contains fifty successful
# login attempts.
# 
# Given that the three characters are always asked for
# in order, analyse the file so as to determine the
# shortest possible secret passcode of unknown length.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

def solve():
        start = time()
        chdir("textfiles")
        file = open("p079_keylog.txt")
        matrix = []
        for line in file:
                matrix.append(line.strip())
        nums = []
        for code in matrix:
                for index in range(len(code)):
                        if code[index] not in nums:
                                nums.append(code[index])
        result = ''
        while len(nums) > 0:
                for i in range(len(nums)):
                        for j in range(len(matrix)):
                                if nums[i] in matrix[j] and matrix[j][0] != nums[i]:
                                        break
                        else:
                                for j in range(len(matrix)):
                                        if len(matrix[j]) > 0 and matrix[j][0] == nums[i]:
                                                matrix[j] = matrix[j][1:]
                                result += nums[i]
                                del nums[i]
                                break
        peresult(79, result, time() - start)

if __name__ == "__main__":
        solve()
