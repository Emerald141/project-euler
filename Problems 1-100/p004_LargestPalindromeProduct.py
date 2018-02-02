# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    largest_palindrome = 0
    for small in range(100, 1000):
        for large in range(max(small, largest_palindrome // small + 1), 1000):
            possible_palindrome = small * large
            if possible_palindrome > largest_palindrome \
             and str(possible_palindrome) == str(possible_palindrome)[::-1]:
                largest_palindrome = possible_palindrome
    return largest_palindrome

if __name__ == "__main__":
    start = time()
    peresult(4, solve(), time() - start)
