##A composite number can be factored many different ways. For instance, not
##including multiplication by one, 24 can be factored in 7 distinct ways:
##
##24 = 2x2x2x3
##24 = 2x3x4
##24 = 2x2x6
##24 = 4x6
##24 = 3x8
##24 = 2x12
##24 = 24
##Recall that the digital root of a number, in base 10, is found by adding
##together the digits of that number, and repeating that process until a
##number is arrived at that is less than 10. Thus the digital root of 467 is 8.
##
##We shall call a Digital Root Sum (DRS) the sum of the digital roots of
##the individual factors of our number.
##The chart below demonstrates all of the DRS values for 24.
##
##Factorisation	Digital Root Sum
##2x2x2x3
##9
##2x3x4
##9
##2x2x6
##10
##4x6
##10
##3x8
##11
##2x12
##5
##24
##6
##The maximum Digital Root Sum of 24 is 11.
##The function mdrs(n) gives the maximum Digital Root Sum of n.
##So mdrs(24)=11.
##Find ∑mdrs(n) for 1 < n < 1,000,000.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def findDigitalRoot(number):
    if number % 9 == 0:
        return 9
    return number % 9

def solve(cap):
    start = time()
    result = 0
    # This list keeps track of all the values of mdrs.
    # It iterates upward: after computing the mdrs of i, it
    # computes the possible mdrs of all multiples of i up to i^2.
    # If the multiples new possible mdrs exceeds its current mdrs,
    # the value is replaced. Else, the old value is kept.
    mdrs = [0 for x in range(cap)]
    for base in range(2, cap):
        if mdrs[base] == 0:
            # base must be prime; not encountered as a multiple of anything
            mdrs[base] = findDigitalRoot(base)
            result += mdrs[base]
        else:
            if findDigitalRoot(base) > mdrs[base]:
                mdrs[base] = findDigitalRoot(base)
            result += mdrs[base]
        multiple = base
        for factor in range(2, base + 1):
            multiple += base
            if multiple >= cap:
                break
            mdrs[multiple] = max(mdrs[multiple], mdrs[base] + mdrs[factor])
    peresult(159, result, time() - start)

if __name__ == "__main__":
    solve(10 ** 6)
