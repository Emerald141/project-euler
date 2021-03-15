# A positive number is pandigital in base b if it contains all digits
# from 0 to b - 1 at least once when written in base b.
#
# A n-super-pandigital number is a number that is simultaneously
# pandigital in all bases from 2 to n inclusively.
# For example 978 = 1111010010_2 = 1100020_3 = 33102_4 = 12403_5 is the
# smallest 5-super-pandigital number.
# Similarly, 1093265784 is the smallest 10-super-pandigital number.
# The sum of the 10 smallest 10-super-pandigital numbers is 20319792309.
#
# What is the sum of the 10 smallest 12-super-pandigital numbers?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from itertools import permutations

# Test whether a number n is pandigital in base b.
def is_factorial(b, n):
    found = [False for i in range(b)]
    while n > 0:
        found[n % b] = True
        n //= b
    return sum(found) == b

# Convert a string representing a base 12 number to a base 10 number
def b12_to_b10(n_str):
    r = 0
    for i in range(len(n_str)):
        r *= 12
        if n_str[i] == 'A':
            r += 10
        elif n_str[i] == 'B':
            r += 11
        else:
            r += int(n_str[i])
    return r

def solve():
    result = 0
    count = 0
    digits = '0123456789AB'
    for first_index in range(1, 12):
        other_digits = digits[:first_index] + digits[first_index + 1:]
        for perm in permutations(other_digits):
            n_str = digits[first_index] + ''.join(perm)
            n = b12_to_b10(n_str)
            for b in range(11, 1, -1):  # Don't have to check base 12
                if not is_factorial(b, n):
                    break
            else:
                print(n_str, n)
                result += n
                count += 1
                if count == 10:
                    return result

if __name__ == "__main__":
    start = time()
    peresult(571, solve(), time() - start)
