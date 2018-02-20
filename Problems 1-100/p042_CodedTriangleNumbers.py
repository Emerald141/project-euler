# The nth term of the sequence of triangle numbers is given by,
# t_n = n * (n + 1) / 2; so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding
# to its alphabetical position and adding these values we form
# a word value. For example, the word value for SKY is
# 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number
# then we shall call the word a triangle word.
#
# Using words.txt, a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def solve():
    word_file = open("../textfiles/p042_words.txt", 'r')
    long_string = word_file.readline()[1:-1]  # Eliminating quote marks at ends
    word_list = long_string.split('","')
    offset = ord('A') - 1
    result = 0
    for word in word_list:
        word_sum = 0
        for char in word:
            word_sum += ord(char) - offset
        if (-1 + sqrt(1 + 8 * word_sum)) / 2 % 1 == 0:
            result += 1
    word_file.close()
    return result

if __name__ == "__main__":
    start = time()
    peresult(42, solve(), time() - start)
