# We define 123-numbers as follows:
#
# 1 is the smallest 123-number.
# When written in base 10 the only digits that can be present are "1", "2" and
# "3" and if present the number of times they each occur is also a 123-number.
# So 2 is a 123-number, since it consists of one digit "2" and 1 is a
# 123-number. Therefore, 33 is a 123-number as well since it consists of two
# digits "3" and 2 is a 123-number.
# On the other hand, 1111 is not a 123-number, since it contains 4 digits
# "1" and 4 is not a 123-number.
#
# In ascending order, the first 123-numbers are:
# 1,2,3,11,12,13,21,22,23,31,32,33,111,112,113,121,122,123,131,...
#
# Let F(n) be the n-th 123-number. For example F(4)=11, F(10)=31, F(40)=1112,
# F(1000)=1223321 and F(6000)=2333333333323.
#
# Find F(111111111111222333). Give your answer modulo 123123123.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(target = 111111111111222333, mod = 123123123):
    # Step 0: Set up factorials
    f = [1]
    for i in range(1, 100):
        f.append(f[-1] * i)
    # Step 1: Find out how many 123-numbers are less than 10^k
    indexes = [0,1,2,3,11,12,13,21,22,23,31,32,33]
    counts = [0 for x in range(100)]
    for c1 in indexes:
        for c2 in indexes:
            for c3 in indexes:
                counts[c1+c2+c3] += f[c1+c2+c3] // (f[c1] * f[c2] * f[c3])
    n = 1  # 0 is not a 123-number.
    while True:
        if counts[n] < target:
            target -= counts[n]
            n += 1
        else:
            break
    # Step 2: Find the 'target'-th 123-number with 'n' digits.
    result = 0
    lock1, lock2, lock3 = 0, 0, 0  # No. of each left of the rightmost n digits
    while n > 0:
        # First, let's see how many such numbers begin with a 1...
        subtotal = 0
        for i1 in indexes:  # Count of 1's in the entire number
            c1 = i1 - lock1 - 1  # Count of 1's in the last n-1 digits
            if c1 < 0:
                continue
            for i2 in indexes:  # Count of 2's in the entire number
                c2 = i2 - lock2  # Count of 2's in the last n-1 digits
                if c2 < 0:
                    continue
                c3 = n - 1 - c1 - c2  # Count of 3's in the last n-1 digits
                if c3 < 0:
                    continue
                i3 = c3 + lock3
                if i3 not in indexes:
                    continue
                subtotal += f[n-1] // (f[c1] * f[c2] * f[c3])
        if subtotal >= target:
            # yep! it begins with a 1
            result = result * 10 + 1
            lock1 += 1
            n -= 1
            continue
        # If that didn't work, let's see if it begins with a 2...
        target -= subtotal
        subtotal = 0
        for i2 in indexes:  # Count of 2's in the entire number
            c2 = i2 - lock2 - 1  # Count of 2's in the last n-1 digits
            if c2 < 0:
                continue
            for i1 in indexes:  # Count of 1's in the entire number
                c1 = i1 - lock1  # Count of 1's in the last n-1 digits
                if c1 < 0:
                    continue
                c3 = n - 1 - c1 - c2  # Count of 3's in the last n-1 digits
                if c3 < 0:
                    continue
                i3 = c3 + lock3
                if i3 not in indexes:
                    continue
                subtotal += f[n-1] // (f[c1] * f[c2] * f[c3])
        if subtotal >= target:
            # yep! it begins with a 2
            result = result * 10 + 2
            lock2 += 1
            n -= 1
            continue
        # If that didn't work, it has to begin with a 3. Process of elimination
        target -= subtotal
        result = result * 10 + 3
        lock3 += 1
        n -= 1
        continue
    return result % mod

if __name__ == "__main__":
    start = time()
    peresult(698, solve(), time() - start)
