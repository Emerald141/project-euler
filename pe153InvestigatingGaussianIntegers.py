##Find the sum of the Gaussian integer divisors
##of the first 10**8 positive integers.

from time import time
from peresult import peresult

def pe153():
    start = time()
    cap = 9
    result = 0
    for a in range(1, 4):
        result += cap // a * a
        b = 1
        while (a ** 2 + b ** 2 <= cap):
            result += 2 * a * (cap // (a ** 2 + b ** 2))
            b += 1
        low = (cap // (a+1)) + 1
        high = cap // a
        result += a * (high - low + 1) * (low + high) // 2
    result -= cap #counted twice
    peresult(153, result, time() - start)

if __name__ == "__main__":
    pe153()
