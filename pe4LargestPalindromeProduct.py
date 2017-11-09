##A palindromic number reads the same both ways. The largest palindrome
##made from the product of two 2-digit numbers is 9009 = 91 × 99.
##
##Find the largest palindrome made from the product of two 3-digit numbers.

from time import time
from peresult import peresult

def pe4():
        start = time()
        largestpalindrome = 0
        for smaller in range(100, 1000):
                for larger in range(max(smaller, largestpalindrome // smaller + 1), 1000):
                        possipal = smaller * larger
                        if possipal < 100000:
                                if possipal // 10000 == possipal % 10 and possipal // 1000 % 10 == possipal // 10 % 10:
                                        largestpalindrome = possipal
                        else:
                                if possipal // 100000 == possipal % 10 and possipal // 10000 % 10 == possipal // 10 % 10 and possipal // 1000 % 10 == possipal // 100 % 10:
                                        largestpalindrome = possipal
        peresult(4, largestpalindrome, time() - start)
        
if __name__ == "__main__":
        pe4()
