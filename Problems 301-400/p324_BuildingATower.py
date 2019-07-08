# Let f(n) represent the number of ways one can fill a 3x3xn tower with
# blocks of 2x1x1.
# You're allowed to rotate the blocks in any way you like; however,
# rotations, reflections etc of the tower itself are counted as distinct.
#
# For example (with q = 100000007) :
# f(2) = 229,
# f(4) = 117805,
# f(10) mod q = 96149360,
# f(10^3) mod q = 24806056,
# f(10^6) mod q = 30808124.
#
# Find f(10^10000) mod 100000007.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from matrixfns import matrixmult, matrixpow
from itertools import product
from math import log

def rot(con):
	# Rotates a config 90 degrees clockwise.
	old_bits = [(con // (2 ** i)) % 2 for i in range(9)]
	new_bits = [old_bits[i] for i in (6, 3, 0, 7, 4, 1, 8, 5, 2)]
	return sum([new_bits[i] * 2 ** i for i in range(9)])

def reflect(con):
	# Reflects a config horizontally.
	old_bits = [(con // (2 ** i)) % 2 for i in range(9)]
	new_bits = [old_bits[i] for i in (6, 7, 8, 3, 4, 5, 0, 1, 2)]
	return sum([new_bits[i] * 2 ** i for i in range(9)])

def solve(cap = 10 ** 10000):
	# Assume that "cap" is divisible by 4.
	mod = 100000007
	# Step 1: Get the "true" configs for all 512 configs
	truecon = [512 for con in range(512)]
	all_truecons = []
	for con in range(512):
		for con1 in [con, rot(con), rot(rot(con)), rot(rot(rot(con)))]:
			for con2 in [con1, reflect(con1)]:
				truecon[con] = min(truecon[con], con2)
		if con == truecon[con]:
			all_truecons.append(con)
	# Step 2: Get the number of ways to tile each config
	tileways = [0 for con in range(512)]
	for con in range(512):
		if truecon[con] != con:
			tileways[con] = tileways[truecon[con]]
			continue
		bits = [(con // (2 ** i)) % 2 for i in range(9)]
		for tiling in product('DRx', repeat=9):
			for bit in range(9):
				if bits[bit] and tiling[bit] != 'x':
					break
				if tiling[bit] == 'D' and (bit > 5 or tiling[bit + 3] != 'x'):
					break
				if tiling[bit] == 'R' and (bit % 3 == 2 or tiling[bit + 1] != 'x'):
					break
				if tiling[bit] == 'x' and sum([bit % 3 > 0 and tiling[bit - 1] == 'R', bit > 2 and tiling[bit - 3] == 'D', bits[bit]]) != 1:
					break
			else:
				tileways[con] += 1
	# Step 3: Construct the adjacency matrix between true configs
	mat = [ [0 for i in range(len(all_truecons))] for j in range(len(all_truecons))]
	for i in range(len(all_truecons)):
		con1 = all_truecons[i]
		for con2 in range(512):
			j = all_truecons.index(truecon[con2])
			if (con1 & con2) == 0:
				mat[i][j] += tileways[con1 | con2]
	# Step 4: Identify and eliminate all redundant states
	mat = matrixmult(mat, mat)
	index = 0
	while index < len(mat):
		if mat[0][index] == 0:
			for row in range(len(mat)):
				mat[row].pop(index)
			mat.pop(index)
		else:
			index += 1
	# Step 5: Use the matrix to solve (Strategy lifted from problem 458)
	rowvector = [[1] + [0 for con in range(1, len(mat))]]
	rowvector = matrixmult(rowvector, matrixpow(mat, cap // 2, mod))
	return rowvector[0][0]

if __name__ == "__main__":
	start = time()
	peresult(324, solve(), time() - start)
