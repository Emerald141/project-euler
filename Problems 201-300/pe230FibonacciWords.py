# For any two strings of digits, A and B, we define F(A,B) to be the sequence
# (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the
# previous two.
# 
# Further, we define D(A,B)(n) to be the n'th digit in the first term of F(A,B)
# that contains at least n digits.
# 
# Example:
# 
# Let A=1415926535, B=8979323846. We wish to find D(A,B)(35), say.
# 
# The first few terms of F(A,B) are:
# 1415926535
# 8979323846
# 14159265358979323846
# 897932384614159265358979323846
# 14159265358979323846897932384614159265358979323846
# 
# Then D(A,B)(35) is the 35th digit in the fifth term, which is 9.
# 
# Now we use for A the first 100 digits of pi behind the decimal point:
# 
# 14159265358979323846264338327950288419716939937510 
# 58209749445923078164062862089986280348253421170679
# 
# and for B the next hundred digits:
# 
# 82148086513282306647093844609550582231725359408128 
# 48111745028410270193852110555964462294895493038196 .
# 
# Find ∑_{n = 0,1,...,17}   10^n * D(A,B)((127+19n)*7^n) .

# THEORY:
#
# Let F(A,B)[k] be the k'th term of F(A,B).
# Consider the x'th digit of F(A,B)[k].
# If x <= len(F(A,B)[k-2]), then this digit is the x'th digit of F(A,B)[k-2].
# Otherwise, it's the (x - len(F(A,B)[k-2]))'th digit of F(A,B)[k-1].

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    a = "14159265358979323846264338327950288419716939937510" \
        + "58209749445923078164062862089986280348253421170679"
    b = "82148086513282306647093844609550582231725359408128" \
        + "48111745028410270193852110555964462294895493038196"
    fibo_lens = [len(a), len(b)]
    result = ""
    for power in range(18):
        str_index = (127 + 19 * power) * (7 ** power)
        while fibo_lens[-1] < str_index:
            fibo_lens.append(fibo_lens[-2] + fibo_lens[-1])
        fibo_index = len(fibo_lens) - 1
        while fibo_index > 1:
            if str_index > fibo_lens[fibo_index - 2]:
                str_index -= fibo_lens[fibo_index - 2]
                fibo_index -= 1
            else:
                fibo_index -= 2
        if fibo_index == 0:
            result = a[str_index - 1] + result
        else:
            result = b[str_index - 1] + result
    peresult(230, result, time() - start)

if __name__ == "__main__":
    solve()
