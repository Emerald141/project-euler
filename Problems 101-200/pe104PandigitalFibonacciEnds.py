##The Fibonacci sequence is defined by the recurrence relation:
##
##F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
##It turns out that F(541), which contains 113 digits, is the first
##Fibonacci number for which the last nine digits are 1-9 pandigital
##(contain all the digits 1 to 9, but not necessarily in order).
##And F(2749), which contains 575 digits, is the first Fibonacci number
##for which the first nine digits are 1-9 pandigital.
##
##Given that F(k) is the first Fibonacci number for which the first nine
##digits AND the last nine digits are 1-9 pandigital, find k.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import log10

def solve():
    start = time()
    print("Note: This one takes around 80 seconds. It's a bit over the limit" \
          + " but I'm working in Python here, so whatchagonnado.")
    k = 2
    fiboCurrent, fiboLast = 1, 1
    while True:
        k += 1
        fiboCurrent, fiboLast = fiboCurrent + fiboLast, fiboCurrent
        lastnine = set(str(fiboCurrent % (10**9)))
        if len(lastnine) == 9 and '0' not in lastnine:
            firstnine = set(str(fiboCurrent // 10**int(log10(fiboCurrent) - 8)))
            if len(firstnine) == 9 and '0' not in firstnine:
                break
    peresult(104, k, time() - start)

if __name__ == "__main__":
    solve()
