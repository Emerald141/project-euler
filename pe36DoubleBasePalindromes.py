##The decimal number, 585 = 10010010012 (binary), is
##palindromic in both bases.
##
##Find the sum of all numbers, less than one million,
##which are palindromic in base 10 and base 2.
##
##(Please note that the palindromic number, in either
##base, may not include leading zeros.)

from time import time
from peresult import peresult
from numassemble import numassemble

def pe36():
        start = time()
        result = 0
        for a in range(1, 10):
                onebin = bin(a)[2:]
                if isPalindrome(onebin):
                        result += a
                twodec = numassemble(a, a)
                twobin = bin(twodec)[2:]
                if isPalindrome(twobin):
                        result += twodec
                for b in range(10):
                        threedec = numassemble(a, b, a)
                        threebin = bin(threedec)[2:]
                        if isPalindrome(threebin):
                                result += threedec
                        fourdec = numassemble(a, b, b, a)
                        fourbin = bin(fourdec)[2:]
                        if isPalindrome(fourbin):
                                result += fourdec
                        for c in range(10):
                                fivedec = numassemble(a, b, c, b, a)
                                fivebin = bin(fivedec)[2:]
                                if isPalindrome(fivebin):
                                        result += fivedec
                                sixdec = numassemble(a, b, c, c, b, a)
                                sixbin = bin(sixdec)[2:]
                                if isPalindrome(sixbin):
                                        result += sixdec
        peresult(36, result, time() - start)

def isPalindrome(string):
        i = 0
        while i < len(string) - 1 - i:
                if string[i] != string[-1-i]:
                        return False
                i += 1
        return True

if __name__ == "__main__":
        pe36()
