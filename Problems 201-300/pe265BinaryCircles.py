##2N binary digits can be placed in a circle so that all
##the N-digit clockwise subsequences are distinct.
##
##For N=3, two such circular arrangements are possible,
##ignoring rotations.
##
##For the first arrangement, the 3-digit subsequences,
##in clockwise order, are:
##000, 001, 010, 101, 011, 111, 110 and 100.
##
##Each circular arrangement can be encoded as a number
##by concatenating the binary digits starting with the
##subsequence of all zeros as the most significant bits
##and proceeding clockwise. The two arrangements for N=3
##are thus represented as 23 and 29:
##
##0b00010111  = 23
##0b00011101  = 29
##Calling S(N) the sum of the unique numeric representations,
##we can see that S(3) = 23 + 29 = 52.
##
##Find S(5).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        strings = ["00000"]
        for newstringlength in range(6, 33):
                newstrings = []
                for string in strings:
                        for newdigit in ('0', '1'):
                                if string[-4:] + newdigit in string:
                                        continue
                                newstrings.append(string + newdigit)
                strings = newstrings
        for ind in range(len(strings) - 1, -1, -1):
                for startpoint in range(1, 5):
                        sequence = strings[ind][-startpoint:] + strings[ind][:5 - startpoint]
                        if sequence in strings[ind]:
                                del strings[ind]
                                break
        result = 0
        for string in strings:
                result += int(string, base=2)
        peresult(265, result, time() - start)

if __name__ == "__main__":
        solve()
