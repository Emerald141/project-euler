# Consider a directed graph made from an orthogonal lattice of H×W nodes.
# The edges are the horizontal and vertical connections between adjacent
# nodes. W vertical directed lines are drawn and all the edges on these
# lines inherit that direction. Similarly, H horizontal directed lines
# are drawn and all the edges on these lines inherit that direction.
#
# Two nodes, A and B in a directed graph, are strongly connected if there
# is both a path, along the directed edges, from A to B as well as from
# B to A. Note that every node is strongly connected to itself.
#
# A strongly connected component in a directed graph is a non-empty set M
# of nodes satisfying the following two properties:
#
# All nodes in M are strongly connected to each other.
# M is maximal, in the sense that no node in M is strongly connected to
# any node outside of M.
# There are 2H×2W ways of drawing the directed lines. Each way gives a
# directed graph G. We define S(G) to be the number of strongly connected
# components in G.
#
# Define C(H,W) to be the sum of S(G) for all possible graphs on a grid
# of H×W. You are given C(3,3)=408, C(3,6)=4696 and
# C(10,20)≡988971143(mod1000000007).
#
# Find C(10000,20000) giving your answer modulo 1000000007.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(m=10000,n=20000):
    result = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            a = (2**(m-1) - 2**(m-i)) * (2**n - 2**(n-j) - 2**(j-1))
            b = (2**(m-1) - 2**(i-1)) * (2**n - 2**(n-j+1) - 2**(j-1) + 1)
            ab = (2**(i-1) - 1) * (2**(m-i) - 1) * (2**(n-j)-1)
            if j == 1:
                ab *= 2**(j-1) - 1
            else:
                ab *= (2**(j-1) - 1) + (2**(j-1) - 2)
            term = 2 * (2**(m+n-1) - a - b + ab)
            print(i,j,a,b,ab, term, sep='\t')
            result += term
    return result

if __name__ == "__main__":
    start = time()
    peresult(716, solve(3,3), time() - start)
