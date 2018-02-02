# A unit fraction contains 1 in the numerator. The decimal
# representation of the unit fractions with denominators
# 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# 
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring
# cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the
# longest recurring cycle in its decimal fraction part.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        longest = 0
        longestindex = 0
        for x in range(1, 1000):
                subtracted = 10
                subtracteds = [10]
                while True:
                        subtracted %= x
                        subtracted *= 10
                        if subtracted in subtracteds:
                                cycLen = len(subtracteds) - subtracteds.index(subtracted)
                                break
                        if subtracted == 0:
                                cycLen = 0
                                break
                        subtracteds.append(subtracted)
                if cycLen > longest:
                        longest = cycLen
                        longestindex = x
        peresult(26, longestindex, time() - start)

if __name__ == "__main__":
        solve()
