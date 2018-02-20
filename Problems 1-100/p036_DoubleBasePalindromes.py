# The decimal number, 585 = 1001001001_2 (binary), is
# palindromic in both bases.
#
# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either
# base, may not include leading zeros.)

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def isPalindrome(string):
    return string == string[::-1]

def solve():
    result = 0
    for a in range(1, 10):
        if isPalindrome(bin(a)[2:]):
            result += a
        two_digs = a * 11
        if isPalindrome(bin(two_digs)[2:]):
            result += two_digs
        for b in range(10):
            three_digs = a * 101 + b * 10
            if isPalindrome(bin(three_digs)[2:]):
                result += three_digs
            four_digs = a * 1001 + b * 110
            if isPalindrome(bin(four_digs)[2:]):
                result += four_digs
            for c in range(10):
                five_digs = a * 10001 + b * 1010 + c * 100
                if isPalindrome(bin(five_digs)[2:]):
                    result += five_digs
                six_digs = a * 100001 + b * 10010 + c * 1100
                if isPalindrome(bin(six_digs)[2:]):
                    result += six_digs
    return result

if __name__ == "__main__":
    start = time()
    peresult(36, solve(), time() - start)
