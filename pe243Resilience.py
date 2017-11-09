##A positive fraction whose numerator is less than its denominator
##is called a proper fraction.
##For any denominator, d, there will be d−1 proper fractions;
##for example, with d = 12:
##1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 ,
##7/12 , 8/12 , 9/12 , 10/12 , 11/12.
##
##We shall call a fraction that cannot be cancelled down a
##resilient fraction.
##Furthermore we shall define the resilience of a denominator,
##R(d), to be the ratio of its proper fractions that are resilient;
##for example, R(12) = 4/11 .
##In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10.
##
##Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

from time import time
from peresult import peresult

def pe70(cap, fraction):
    start = time()
    array = [x for x in range(cap)]
    result = 0
    for x in range(2, len(array)):
        if x == array[x]: #if x is prime
            for multiple in range(2 * x, len(array), x):
                array[multiple] *= (x - 1)
                array[multiple] //= x
        if array[x] / (x-1) < fraction:
            peresult(243, x, time() - start)
            return
    print("Error: No such number below", cap)

if __name__ == "__main__":
    pe70(10 ** 3, 15499/94744)
