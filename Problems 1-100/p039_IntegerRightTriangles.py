# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from math import sqrt

def solve(cap = 1000):
    solution_counts = [0 for index in range(cap + 1)]
    for lesser in range(3, cap // 3):
        greater = lesser + 1
        while True:
            hypotenuse = sqrt(lesser ** 2 + greater ** 2)
            if lesser + greater + hypotenuse > cap:
                break
            if hypotenuse % 1 == 0:
                solution_counts[lesser + greater + int(hypotenuse)] += 1
            greater += 1
    return solution_counts.index(max(solution_counts))

if __name__ == "__main__":
    start = time()
    peresult(39, solve(), time() - start)
