##Take the number 192 and multiply it by each of 1, 2, and 3:
##
##192 × 1 = 192
##192 × 2 = 384
##192 × 3 = 576
##By concatenating each product we get the 1 to 9 pandigital,
##192384576. We will call 192384576 the concatenated product
##of 192 and (1,2,3)
##
##The same can be achieved by starting with 9 and multiplying
##by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which
##is the concatenated product of 9 and (1,2,3,4,5).
##
##What is the largest 1 to 9 pandigital 9-digit number that can
##be formed as the concatenated product of an integer with
##(1,2, ... , n) where n > 1?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from numassemble import numassemble

def solve():
        start = time()
        nums = [8, 7, 6, 5, 4, 3, 2, 1] #The first will be 9
        a = 9
        #Pattern has to be XXXX YYYYY
        #If start with 3-digit number, all remaining will be 4 digit
        #since first number has to be a 9
        #If start with 2-digit number, all remaining will be 3 digit
        #XXX YYYY ZZZZ doesn't work
        #XX YYY ZZZ doesn't work either
        #Can't hit nine total digits without a 4 digit initial value
        for b in nums:
                for c in nums:
                        if c != b:
                                for d in nums:
                                        if d not in [b, c]:
                                                num = numassemble(a, b, c, d)
                                                duonum = num * 2
                                                string = str(num) + str(duonum)
                                                if len(set(string)) == 9 and '0' not in set(string):
                                                        result = int(string)
                                                        break
                                else:
                                        continue
                                break
                else:
                        continue
                break
        if result < 918273645:
                result = 918273645
        peresult(38, result, time() - start)

if __name__ == "__main__":
        solve()
