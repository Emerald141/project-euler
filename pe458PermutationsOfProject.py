##Consider the alphabet A made out of the letters of the word "project":
##A={c,e,j,o,p,r,t}.
##Let T(n) be the number of strings of length n consisting of letters
##from A that do not have a substring that is one of the 5040
##permutations of "project".
##
##T(7)=7^7-7!=818503.
##Find T(10^12). Give the last 9 digits of your answer.

#Strategy heavily adapted from Problem 304.

from time import time
from peresult import peresult

def pe458():
    start = time()
    mod = 10**9
    matpows =[[[1, 6, 0, 0, 0, 0],
               [1, 1, 5, 0, 0, 0],
               [1, 1, 1, 4, 0, 0],
               [1, 1, 1, 1, 3, 0],
               [1, 1, 1, 1, 1, 2],
               [1, 1, 1, 1, 1, 1]]]
    for twopow in range(40): #just to be safe
        newmat = matrixmult(matpows[-1], matpows[-1])
        for row in range(len(newmat)):
            for col in range(len(newmat[0])):
                newmat[row][col] %= mod
        matpows.append(newmat)
    index1 = 10 ** 12 - 1
    rowvector = [[7, 0, 0, 0, 0, 0]]
    while index1 > 0:
        power = 0
        while 2 ** (power + 1) < index1:
            power += 1
        rowvector = matrixmult(rowvector, matpows[power])
        for index in range(len(rowvector[0])):
            rowvector[0][index] %= mod
        index1 -= 2 ** power
    result = sum(rowvector[0]) % mod
    peresult(458, result, time() - start)

def matrixmult(mat1, mat2):
    result = [ [0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
    for row in range(len(result)):
        for col in range(len(result[0])):
            for i in range(len(mat2[0])):
                result[row][col] += mat1[row][i] * mat2[i][col]
    return result

if __name__ == "__main__":
    pe458()
