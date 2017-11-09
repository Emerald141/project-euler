##The divisors of 6 are 1,2,3 and 6.
##The sum of the squares of these numbers is 1+4+9+36=50.
##
##Let sigma2(n) represent the sum of the squares of the divisors of n.
##Thus sigma2(6)=50.
##
##Let SIGMA2 represent the summatory function of sigma2, that is
##SIGMA2(n)=∑sigma2(i) for i=1 to n.
##The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.
##Find SIGMA2(10^15) modulo 10^9.

from time import time
from peresult import peresult

def pe401(n):
    start = time()
    result = 0
    for i in range(1, int(n ** .5) + 1):
        cap = n // i
        result += (cap * (cap + 1) * (2 * cap + 1)) // 6
        result %= 10 ** 9
        largestI = i
    i = 1
    while n // i > largestI:
        result += i ** 2 * (n // i - largestI)
        result %= 10 ** 9
        i += 1
    peresult(401, result, time() - start)
