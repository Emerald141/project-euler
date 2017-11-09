##The number, 1406357289, is a 0 to 9 pandigital number because
##it is made up of each of the digits 0 to 9 in some order, but
##it also has a rather interesting sub-string divisibility property.
##
##Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this
##way, we note the following:
##
##d2d3d4=406 is divisible by 2
##d3d4d5=063 is divisible by 3
##d4d5d6=635 is divisible by 5
##d5d6d7=357 is divisible by 7
##d6d7d8=572 is divisible by 11
##d7d8d9=728 is divisible by 13
##d8d9d10=289 is divisible by 17
##Find the sum of all 0 to 9 pandigital numbers with this property.

from time import time
from peresult import peresult
from listexclude import listexclude
from numassemble import numassemble

def pe43():
        start = time()
        result = 0
        digs = [x for x in range(10)]
        for d1 in digs:
                for d2 in listexclude(digs, d1):
                        for d3 in listexclude(digs, d1, d2):
                                for d4 in listexclude([0, 2, 4, 6, 8], d1, d2, d3):
                                        for d5 in listexclude(digs, d1, d2, d3, d4):
                                                if numassemble(d3,d4,d5) % 3 == 0:
                                                        for d6 in listexclude([0, 5], d1, d2, d3, d4, d5):
                                                                for d7 in listexclude(digs, d1, d2, d3, d4, d5, d6):
                                                                        if numassemble(d5, d6, d7) % 7 == 0:
                                                                                for d8 in listexclude(digs, d1, d2, d3, d4, d5, d6, d7):
                                                                                        if numassemble(d6, d7, d8) % 11 == 0:
                                                                                                for d9 in listexclude(digs, d1, d2, d3, d4, d5, d6, d7, d8):
                                                                                                        if numassemble(d7, d8, d9) % 13 == 0:
                                                                                                                for d10 in listexclude(digs, d1, d2, d3, d4, d5, d6, d7, d8, d9):
                                                                                                                        if numassemble(d8, d9, d10) % 17 == 0:
                                                                                                                                result += numassemble(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
        peresult(43, result, time() - start)
        #This code is not pretty. There's almost certainly a better way.

if __name__ == "__main__":
        pe43()
