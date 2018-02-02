# The nth term of the sequence of triangle numbers is given by,
# tn = ½n(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding
# to its alphabetical position and adding these values we form
# a word value. For example, the word value for SKY is
# 19 + 11 + 25 = 55 = t10. If the word value is a triangle number
# then we shall call the word a triangle word.
# 
# Using words.txt, a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir
from math import sqrt

def solve():
        start = time()
        chdir("textfiles")
        file = open("p042_words.txt")
        longstring = file.readline()
        longstring = longstring[1:-1] #Eliminating " at the ends
        wordlist = longstring.split('","')
        offset = ord('A') - 1
        result = 0
        for word in wordlist:
                wordsum = 0
                for char in word:
                        wordsum += ord(char) - offset
                if (-1 + sqrt(1 + 8 * wordsum)) / 2 % 1 == 0:
                        result += 1
        peresult(42, result, time() - start)

if __name__ == "__main__":
        solve()
