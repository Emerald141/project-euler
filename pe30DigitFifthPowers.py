##Surprisingly there are only three numbers that can
##be written as the sum of fourth powers of their digits:
##
##1634 = 1^4 + 6^4 + 3^4 + 4^4
##8208 = 8^4 + 2^4 + 0^4 + 8^4
##9474 = 9^4 + 4^4 + 7^4 + 4^4
##As 1 = 14 is not a sum it is not included.
##
##The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##
##Find the sum of all the numbers that can be written as
##the sum of fifth powers of their digits.

from time import time
from peresult import peresult

def pe30():
        start = time()
        result = 0
        digpowers = [x ** 5 for x in range(10)]
        for x in range(10, 6 * (9 ** 5)):
                trimmed = x
                powerdigsum = 0
                while trimmed > 0:
                        powerdigsum += digpowers[trimmed % 10]
                        trimmed //= 10
                if powerdigsum == x:
                        result += x
        peresult(30, result, time() - start)

if __name__ == "__main__":
        pe30()
