# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or
# equal to n which are relatively prime to n. For example, as
# 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to
# nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive
# number, so φ(1)=1.
# 
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
# permutation of 79180.
# 
# Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation
# of n and the ratio n/φ(n) produces a minimum.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(cap):
    start = time()
    array = [x for x in range(cap)]
    resultIndex = 0
    resultRatio = len(array) + 1 #guaranteed to be larger
    for x in range(2, len(array)):
        if x == array[x]: #if x is prime
            for multiple in range(2 * x, len(array), x):
                array[multiple] *= (x - 1)
                array[multiple] //= x
        elif arePermutes(x, array[x]) and x / array[x] < resultRatio:
            resultIndex = x
            resultRatio = x / array[x]
    peresult(70, resultIndex, time() - start)

def arePermutes(num1, num2):
    digitarray = [0 for x in range(10)]
    while num1 > 0:
        digitarray[num1 % 10] += 1
        num1 //= 10
    while num2 > 0:
        digitarray[num2 % 10] -= 1
        num2 //= 10
    for i in digitarray:
        if i != 0:
            return False
    return True

if __name__ == "__main__":
    solve(10 ** 7)
