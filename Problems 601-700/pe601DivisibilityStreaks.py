from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    start = time()
    g = 1
    cap = 1
    result = 0
    for iPlusOne in range(2, 33):
        gNew = g
        while gNew % iPlusOne != 0:
            gNew += g
        cap *= 4
        result += (cap - 2) // g
        result -= (cap - 2) // gNew
        g = gNew
    peresult(601, result, time() - start)

if __name__ == "__main__":
    solve()
