##Looking at the table below, it is easy to verify that the maximum
##possible sum of adjacent numbers in any direction (horizontal, vertical,
##diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).
##
##−2	5	3	2
##9	−6	5	1
##3	2	7	3
##−1	8	−4	8
##Now, let us repeat the search, but on a much larger scale:
##
##First, generate four million pseudo-random numbers using a
##specific form of what is known as a "Lagged Fibonacci Generator":
##
##For 1 ≤ k ≤ 55,
##s_k = [100003 − 200003k + 300007k^3] (modulo 1000000) − 500000.
##For 56 ≤ k ≤ 4000000,
##s_k = [s_{k−24} + s_{k−55} + 1000000] (modulo 1000000) − 500000.
##
##Thus, s_10 = −393027 and s_100 = 86613.
##
##The terms of s are then arranged in a 2000×2000 table, using the
##first 2000 numbers to fill the first row (sequentially), the next
##2000 numbers to fill the second row, and so on.
##
##Finally, find the greatest sum of (any number of) adjacent entries
##in any direction (horizontal, vertical, diagonal or anti-diagonal).

from time import time
from peresult import peresult

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LaggedFiboGen:
    def __init__(self):
        self.rear = Node((100003 - 200003 + 300007) % (10**6) - 500000)
        tempFront = self.rear
        for k in range(2, 56):
            tempFront.next = Node((100003 - (200003*k) + (300007*k**3))\
                                  % (10**6) - 500000)
            tempFront = tempFront.next
        self.mid = self.rear
        for x in range(31):
            self.mid = self.mid.next
        self.front = tempFront
    def nextnum(self):
        self.front.next = Node((self.rear.value + self.mid.value + 1000000)\
                               % (10**6) - 500000)
        self.front = self.front.next
        poppedValue = self.rear.value
        temp = self.rear
        self.rear = self.rear.next
        temp.next = None
        self.mid = self.mid.next
        return poppedValue

def maxSumSubsequence1D(sequence):
    maxOverall = sequence[0]
    maxCurrent = sequence[0] #largest subsequence ending at a certain point
    for pointer in range(1, len(sequence)):
        maxCurrent = max(sequence[pointer], maxCurrent + sequence[pointer])
        maxOverall = max(maxCurrent, maxOverall)
    return maxOverall

def pe149():
    start = time()
    gen = LaggedFiboGen()
    horiz = [ [] for x in range(2000)]
    vert = [ [] for x in range(2000)]
    diag = [ [] for x in range(3999)]
    adiag = [ [] for x in range(3999)]
    x, y = 0, 0
    while y < 2000:
        entry = gen.nextnum()
        horiz[y].append(entry)
        vert[x].append(entry)
        diag[x - y + 1999].append(entry)
        adiag[x + y].append(entry)
        x = (x + 1) % 2000
        if x == 0:
            y += 1
    result = 0
    for sequence in horiz + vert + diag + adiag:
        result = max(result, maxSumSubsequence1D(sequence))
    peresult(149, result, time() - start)

if __name__ == "__main__":
    pe149()
