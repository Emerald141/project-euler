##An irrational decimal fraction is created by concatenating
##the positive integers:
##
##0.123456789101112131415161718192021...
##
##It can be seen that the 12th digit of the fractional part is 1.
##
##If dn represents the nth digit of the fractional part, find the
##value of the following expression.
##
##d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        result = 1
        for exp in range(7):
                grandplace = 10 ** exp
                phase = 1
                while grandplace > 10 ** (phase - 1) * 9 * phase:
                        grandplace -= 10 ** (phase - 1) * 9 * phase
                        phase += 1
                plus = (grandplace - 1) // phase
                concatnum = 10 ** (phase - 1) + plus
                smallplace = (grandplace - 1) % phase
                result *= int(str(concatnum)[smallplace])
        peresult(40, result, time() - start)

if __name__ == "__main__":
        solve()
