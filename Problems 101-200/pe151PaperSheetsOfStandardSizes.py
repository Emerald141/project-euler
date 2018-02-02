##A printing shop runs 16 batches (jobs) every week and each batch
##requires a sheet of special colour-proofing paper of size A5.
##
##Every Monday morning, the foreman opens a new envelope, containing
##a large sheet of the special paper with size A1.
##
##He proceeds to cut it in half, thus getting two sheets of size A2. Then
##he cuts one of them in half to get two sheets of size A3 and so on until
##he obtains the A5-size sheet needed for the first batch of the week.
##
##All the unused sheets are placed back in the envelope.
##
##
##At the beginning of each subsequent batch, he takes from the envelope
##one sheet of paper at random. If it is of size A5, he uses it. If it is
##larger, he repeats the 'cut-in-half' procedure until he has what he needs
##and any remaining sheets are always placed back in the envelope.
##
##Excluding the first and last batch of the week, find the expected number
##of times (during each week) that the foreman finds a single sheet of
##paper in the envelope.
##
##Give your answer rounded to six decimal places using the format x.xxxxxx .

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from factorfns import factorizationpow

def solve():
        #At any time there are:
        #Between 0 and 1 A2 sheets
        #Between 0 and 2 A3 sheets
        #Between 0 and 4 A4 sheets
        #Between 0 and 8 A5 sheets
        #Fewer than 4 times the guy could have found a single sheet
        start = time()
        a = [[], []]
        for a2num in a:
                a2num.extend([ [] for a3 in range(3)])
                for a3num in a2num:
                        a3num.extend([ [] for a4 in range(5)])
                        for a4num in a3num:
                                a4num.extend([ [] for a5 in range(9)])
                                for a5num in a4num:
                                        a5num.extend([0 for x in range(4)])
        a[1][1][1][1][0] = 1
        for turn in range(14):
                newa = [[], []]
                for a2num in newa:
                        a2num.extend([ [] for a3 in range(3)])
                        for a3num in a2num:
                                a3num.extend([ [] for a4 in range(5)])
                                for a4num in a3num:
                                        a4num.extend([ [] for a5 in range(9)])
                                        for a5num in a4num:
                                                a5num.extend([0 for x in range(4)])
                smallsums = []
                for a2 in range(len(a)):
                        for a3 in range(len(a[a2])):
                                for a4 in range(len(a[a2][a3])):
                                        for a5 in range(len(a[a2][a3][a4])):
                                                if a2 + a3 + a4 + a5 != 0 and sum(a[a2][a3][a4][a5]) != 0:
                                                        smallsums.append(a2 + a3 + a4 + a5)
                commontotal = lcm(smallsums)
                for a2 in range(len(a)):
                        for a3 in range(len(a[a2])):
                                for a4 in range(len(a[a2][a3])):
                                        for a5 in range(len(a[a2][a3][a4])):
                                                if a2 + a3 + a4 + a5 == 0 or sum(a[a2][a3][a4][a5]) == 0:
                                                        continue
                                                multiplier = commontotal // (a2 + a3 + a4 + a5)
                                                if a2 + a3 + a4 + a5 == 1:
                                                        if a2 == 1:
                                                                newa[0][1][1][1] = matrixsum(newa[0][1][1][1], [0] + matrixmult(multiplier, a[1][0][0][0]))
                                                        elif a3 == 1:
                                                                newa[0][0][1][1] = matrixsum(newa[0][0][1][1], [0] + matrixmult(multiplier, a[0][1][0][0]))
                                                        else: #a4 == 1, there's no way to get to a5 == 1 in 14 turns
                                                                newa[0][0][0][1] = matrixsum(newa[0][0][0][1], [0] + matrixmult(multiplier, a[0][0][1][0]))
                                                else:
                                                        if a2 != 0 and a3 != 2 and a4 != 4 and a5 != 8:
                                                                newa[a2-1][a3+1][a4+1][a5+1] = matrixsum(newa[a2-1][a3+1][a4+1][a5+1], matrixmult(multiplier, a[a2][a3][a4][a5]))
                                                        if a3 != 0 and a4 != 4 and a5 != 8:
                                                                newa[a2][a3-1][a4+1][a5+1] = matrixsum(newa[a2][a3-1][a4+1][a5+1], matrixmult(a3 * multiplier, a[a2][a3][a4][a5]))
                                                        if a4 != 0 and a5 != 8:
                                                                newa[a2][a3][a4-1][a5+1] = matrixsum(newa[a2][a3][a4-1][a5+1], matrixmult(a4 * multiplier, a[a2][a3][a4][a5]))
                                                        if a5 != 0:
                                                                newa[a2][a3][a4][a5-1] = matrixsum(newa[a2][a3][a4][a5-1], matrixmult(a5 * multiplier, a[a2][a3][a4][a5]))
                a = newa
        numerator = 0
        denominator = sum(a[0][0][0][1])
        for ind in range(len(a[0][0][0][1])):
                numerator += ind * a[0][0][0][1][ind]
        result = numerator / denominator
        result *= 10 ** 7
        result = round(result, -1)
        result /= 10 ** 7
        peresult(151, result, time() - start)

def matrixsum(base, *others):
        result = base[:]
        for i in range(len(base)):
                for other in others:
                        result[i] += other[i]
        return result

def matrixmult(multiplier, base):
        result = base[:]
        for i in range(len(result)):
                result[i] *= multiplier
        return result

def lcm(nums):
        masterdict = dict()
        for num in nums:
                numdict = factorizationpow(num)
                for key in numdict.keys():
                        if key in masterdict and masterdict[key] >= numdict[key]:
                                continue
                        masterdict[key] = numdict[key]
        result = 1
        for key in masterdict.keys():
                result *= key ** masterdict[key]
        return result

if __name__ == "__main__":
        solve()
