# A horizontal row comprising of 2n + 1 squares has n red counters
# placed at one end and n blue counters at the other end, being
# separated by a single empty square in the centre. For example, when n = 3.
# 
# RRR_BBB
# 
# A counter can move from one square to the next (slide) or can jump
# over another counter (hop) as long as the square next to that counter
# is unoccupied.
# 
# Let M(n) represent the minimum number of moves/actions to completely
# reverse the positions of the coloured counters; that is, move all the
# red counters to the right and all the blue counters to the left.
# 
# It can be verified M(3) = 15, which also happens to be a triangle number.
# 
# If we create a sequence based on the values of n for which M(n) is a
# triangle number then the first five terms would be: 
# 1, 3, 10, 22, and 63, and their sum would be 99.
# 
# Find the sum of the first forty terms of this sequence.

# THEORY:
# 
# Each of the 2x counters moves x+1 spaces, and a total of x^2 jumps are
# made. Therefore M(x) = x^2 + 2x. If M(x) is equal to the y'th triangle
# number, x^2 + 2x = (y^2 + y) / 2; that is, 2x^2 - y^2 + 4x - y = 0.
# 
# Through use of Dario Alpern's perpetually-handy Diophantine equation solver
# (found at https://www.alpertron.com.ar/QUAD.HTM),
# we find the following recursive formula for (x,y) pairs:
#   x_(n+1) = 3 x_n + 2 y_n + 3
#   y_(n+1) = 4 x_n + 3 y_n + 5
# The (x,y) seeds (0,0) and (1, 2) are enough to generate the lower terms.
# We take 40 terms from each, then take the 40 lowest between them.

from time import time
from peresult import peresult

def pe321(value_count = 40):
    start = time()
    values = set([1])  # To prevent duplication (safety first!)
                       # 1 is not added in the below loop, so it's added here.
    for seed in ( (0,0), (1,2) ):
        x, y = seed[0], seed[1]
        for value in range(value_count):
            x, y = 3 * x + 2 * y + 3, 4 * x + 3 * y + 5
            values.add(x)
    print(sorted(values)[:value_count])
    result = sum(sorted(values)[:value_count])
    peresult(321, result, time() - start)

if __name__ == "__main__":
    pe321()
