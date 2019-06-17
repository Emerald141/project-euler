# Consider the triangle with sides √5, √65 and √68. It can be shown that this
# triangle has area 9.
# 
# S(n) is the sum of the areas of all triangles with sides √(1+b2), √(1+c2)
# and √(b2+c2) (for positive integers b and c ) that have an integral area
# not exceeding n.
# 
# The example triangle has b=2 and c=8.
# 
# S(10^6)=18018206.
# 
# Find S(10^10).

# THEORY:
# 
# Using Heron's formula and some algebraic reduction, it can be determined that
# 4A^2 is even (which it should be!) if and only if b and c are BOTH even.
# So say that b = 2x and c = 2y for some integers x and y.
# Then some further reduction shows that A^2 = x^2 + y^2 + (2xy)^2.
# 
# If y is fixed, then all integral [A, x] pairs can be generated sequentially by
#    [A', x'] == [A, x] * [[8y^2+1, +/-(16y^3+4y)], [+/-(4y), 8y^2+1]]
# for some seed [A, x] pair: either [y, 0] or something computed from a previous
# fixed y. (This isn't based in theory; I figured it out by observation from
# Dario Alpern's ever-helpful Diophantine equation solver.)

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matrixmult

def solve(cap = 10 ** 10):
    seeds = dict()
    solutions = dict()
    finished = False  # Once this is true, just iterate through seeds.
    y = 0
    while True:
        if not finished:
            y += 1
        elif len(seeds.keys()) > 0:
            y = list(seeds.keys())[0]
        else:
            break
        mat1 = [[8 * y ** 2 + 1, 4 * y], [16 * y ** 3 + 4 * y, 8 * y ** 2 + 1]]
        mat2 = [[8 * y ** 2 + 1, -4 * y], [-16 * y ** 3 - 4 * y, 8 * y ** 2 + 1]]
        for cycle in range(len(seeds[y]) + 1 if y in seeds else 1):
            if cycle == 0:
                if finished:
                    continue
                seed = [y, 0]
            else:
                seed = seeds[y][cycle - 1]
            print("Seed:", seed)
            # seed = [A', x']
            for mat in [mat1, mat2]:
                if mat == mat2 and cycle == 0:
                    break  # Redundant.
                c = seed[:]
                while True:
                    c = matrixmult([c], mat)[0]
                    if abs(c[0]) <= cap:
                        print('\t', c)
                        if y not in solutions:
                            solutions[y] = [abs(c[0])]
                        elif abs(c[0]) not in solutions[y]:
                            solutions[y].append(abs(c[0]))
                        if abs(c[1]) not in seeds:
                            seeds[abs(c[1])] = [[c[0], y]]
                        elif [c[0],y] not in seeds[abs(c[1])]:
                            seeds[abs(c[1])].append([c[0],y])
                    else:
                        break
        if 8 * y ** 3 + y > cap:
            finished = True
        if y in seeds:
            seeds.pop(y)
    result = 0
    for x in solutions:
        result += sum(solutions[x])
    return result

if __name__ == "__main__":
    start = time()
    peresult(390, solve(10 ** 10), time() - start)
