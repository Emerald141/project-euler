# By replacing each of the letters in the word CARE with
# 1, 2, 9, and 6 respectively, we form a square number:
# 1296 = 362. What is remarkable is that, by using the same
# digital substitutions, the anagram, RACE, also forms a
# square number: 9216 = 962. We shall call CARE (and RACE) a
# square anagram word pair and specify further that leading
# zeroes are not permitted, neither may a different letter
# have the same digital value as another letter.
# 
# Using words.txt, a 16K text file containing nearly two-thousand
# common English words, find all the square anagram word pairs
# (a palindromic word is NOT considered to be an anagram of itself).
# 
# What is the largest square number formed by any member of such a pair?
# 
# NOTE: All anagrams formed must be contained in the given text file.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir
from digitfns import digitcount
from math import sqrt

def solve():
        start = time()
        chdir("textfiles")
        file = open("p098_words.txt")
        for line in file:
                words = line[1:-1].split('","')
        sortedlists = []
        for word in words:
                sortedlists.append(sorted(word))
        pairs = []
        for ind1 in range(len(words) - 1):
                for ind2 in range(ind1 + 1, len(words)):
                        if sortedlists[ind1] == sortedlists[ind2]:
                                pairs.append([words[ind1], words[ind2]])
        largest = 0
        for pair in pairs:
                length = len(pair[0])
                if digitcount(largest) > length:
                        continue
                maxbase = int(sqrt(10 ** length)) - 1
                minbase = int(sqrt(10 ** (length - 1)))
                for base in range(maxbase, minbase - 1, -1):
                        square = str(base ** 2)
                        letterDict = dict()
                        assignedDigits = []
                        for index in range(len(pair[0])):
                                digit = int(square[index])
                                letter = pair[0][index]
                                if digit in assignedDigits and letter not in letterDict.keys():
                                        break
                                if letter in letterDict.keys() and letterDict[letter] != digit:
                                        break
                                assignedDigits.append(digit)
                                letterDict[letter] = digit
                        else:
                                if letterDict[pair[1][0]] == 0:
                                        continue
                                newsquare = 0
                                for letter in pair[1]:
                                        newsquare *= 10
                                        newsquare += letterDict[letter]
                                if sqrt(newsquare) % 1 == 0:
                                        largest = max(largest, newsquare, int(square))
                                        print(pair[0], '=', square, 'and', pair[1], '=', newsquare)
                                        break
        peresult(98, largest, time() - start)

if __name__ == "__main__":
        solve()
