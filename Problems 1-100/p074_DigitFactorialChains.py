##The number 145 is well known for the property that the sum of the
##factorial of its digits is equal to 145:
##
##1! + 4! + 5! = 1 + 24 + 120 = 145
##
##Perhaps less well known is 169, in that it produces the longest chain
##of numbers that link back to 169; it turns out that there are only three
##such loops that exist:
##
##169 → 363601 → 1454 → 169
##871 → 45361 → 871
##872 → 45362 → 872
##
##It is not difficult to prove that EVERY starting number will eventually
##get stuck in a loop. For example,
##
##69 → 363600 → 1454 → 169 → 363601 (→ 1454)
##78 → 45360 → 871 → 45361 (→ 871)
##540 → 145 (→ 145)
##
##Starting with 69 produces a chain of five non-repeating terms, but the
##longest non-repeating chain with a starting number below one million is
##sixty terms.
##
##How many chains, with a starting number below one million, contain exactly
##sixty non-repeating terms?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    factorials = [1]
    for x in range(1, 10):
        factorials.append(factorials[-1] * x)
    def nextlink(num): #I love that you can do this
        link = 0
        while num > 0:
            link += factorials[num % 10]
            num //= 10
        return link
    rep1 = [0, 1, 2, 145, 40585]
    rep2 = [871, 45361, 872, 45362]
    rep3 = [169, 363601, 1454]
    repeats = rep1 + rep2 + rep3
    result = 0
    for startnum in range(1, 10**6):
        link = startnum
        for step in range(59):
            link = nextlink(link)
            if link in repeats:
                if (step == 56 and link in rep3):
                    result += 1
                elif (step == 57 and link in rep2):
                    result += 1
                elif (step == 58 and link in rep1):
                    result += 1
                else:
                    break
    peresult(74, result, time() - start)

if __name__ == "__main__":
    solve()
