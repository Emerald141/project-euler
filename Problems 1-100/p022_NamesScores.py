# Using names.txt (right click and 'Save Link/Target As...'), a
# 46K text file containing over five-thousand first names, begin
# by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    file = open("../textfiles/p022_names.txt")
    longstring = file.readline()[1:-1]  # Eliminating quote marks at ends
    namelist = sorted(longstring.split('","'))
    offset = ord('A') - 1
    result = 0
    for index in range(len(namelist)):
        namescore = 0
        for char in namelist[index]:
            namescore += ord(char) - offset
        result += namescore * (index + 1)
    return result

if __name__ == "__main__":
    start = time()
    peresult(22, solve(), time() - start)
