##12n musicians participate at a music festival. On the first day, they
##form 3n quartets and practice all day.
##
##It is a disaster. At the end of the day, all musicians decide they will
##never again agree to play with any member of their quartet.
##
##On the second day, they form 4n trios, each musician avoiding his previous
##quartet partners.
##
##Let f(12n) be the number of ways to organize the trios amongst the 12n
##musicians.
##
##You are given f(12) = 576 and f(24) mod 1 000 000 007 = 509089824.
##
##Find f(600) mod 1 000 000 007.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(twelveN):
    start = time()
    mod = 1000000007
    n = twelveN // 12
    factorial = [1 for i in range(4 * n + 1)]
    for i in range(2, len(factorial)):
        factorial[i] = factorial[i-1] * i
    choices = [[factorial[large] // factorial[large-small]\
               for small in range(5)] for large in range(4 * n + 1)]
    permutes = [ [ [0 for x in range(4*n + 1)] for y in range(4*n+1)] \
                  for z in range(4*n + 1)]
    permutes[4*n][0][0] = 1
    for k in range(0, 12 * n, 4):
        for a in range((12 * n - k) // 3 + 1):
            for b in range(min((12 * n - k - 3 * a) // 2 + 1, 4 * n + 1)):
                c = 12 * n - k - 3 * a - 2 * b
                if c not in range(4*n + 1):
                    continue
                if 4*n - a - b - c < 0:
                    continue
                for fromA in range(5):
                    for fromB in range(5):
                        fromC = 4 - fromA - fromB
                        if fromC < 0:
                            continue
                        if a - fromA in range(4*n + 1) \
                           and b + fromA - fromB in range(4*n + 1) and b >= fromB\
                           and c + fromB - fromC in range(4*n + 1) and c >= fromC:
                            permutes[a-fromA][b+fromA-fromB][c+fromB-fromC] += \
                                permutes[a][b][c] \
                                * choices[a][fromA] * choices[b][fromB] \
                                * choices[c][fromC] * 24 // factorial[fromA] \
                                // factorial[fromB] // factorial[fromC]
    result = permutes[0][0][0] // factorial[4 * n] % mod
    peresult(475, result, time() - start)

if __name__ == "__main__":
    solve(600)
