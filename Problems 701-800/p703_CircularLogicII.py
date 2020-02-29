# Given an integer n, n≥3, let B={false,true} and let B^n be the set of
# sequences of n values from B. The function f from B^n to B^n is defined
# by f(b_1…b_n)=c1…cn where:
#
# c_i = b_i + 1 for 1≤i<n.
# c_n = b_1 AND (b_2 XOR b_3), where AND and XOR are the logical AND and
# exclusive OR operations.
#
# Let S(n) be the number of functions T from B^n to B such that for all x in
# B^n, T(x) AND T(f(x))=false. You are given that S(3)=35 and S(4)=2118.
#
# Find S(20). Give your answer modulo 1001001011.

# THEORY:
#
# Reinterpret B^n as the set of nonnegative integers less than 2^n.
# Consider a graph whose nodes are these numbers, with edges given by f.
# This will be a forest of graphs which each have a single loop of recurrent
# states; each recurrent state may be the head of a tree leading to it.
# The problem becomes finding the number of ways to color this graph red and
# black such that no two consecutive nodes are red.
#
# For each recurrent state, find the number of ways the subtree can be colored
# if that node is red, and the number of ways it can be colored if that node
# is black.
# Then, assume the first node in the recurrent loop is red, and advance to find
# the number of configurations with the final node in the loop black.
# Follow this by assuming the first node is black. The final node can be either
# red or black.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve(n = 20):
    # Step 0: Set up the function f and its inverses, and the tree counting fn.
    mod = 1001001011
    def f(x):
        return x // 2 + 2 ** (n - 1) * ((x % 8) in [3, 5])
    def first_child(x):  # The first inverse of f
        code = (x % 4) + (x // (2 ** (n - 1))) * 4
        trimmed = (x * 2) % (2 ** n)
        if code in [0, 1, 2, 3]:
            return trimmed
        elif code in [5, 6]:
            return trimmed + 1
        else:
            return -1
    def second_child(x):  # The second inverse of f
        code = (x % 4) + (x // (2 ** (n - 1))) * 4
        trimmed = (x * 2) % (2 ** n)
        if code in [0, 3]:
            return trimmed + 1
        else:
            return -1
    def count_configs(x):  # Count colorings of x's subtree. Root = [red, black]
        child = first_child(x)
        if child == -1:
            return [1, 1]
        child_configs = count_configs(child)
        result = [child_configs[1] % mod, sum(child_configs) % mod]
        child = second_child(x)
        if child == -1:
            return result
        child_configs = count_configs(child)
        return [(result[0] * child_configs[1]) % mod, (result[1] * sum(child_configs)) % mod]
    # Step 1: Find all the recurrent states.
    recurrent = [True for x in range(2 ** n)]
    while True:
        new_recurrent = [False for x in range(2 ** n)]
        for x in range(2 ** n):
            if recurrent[x]:
                new_recurrent[f(x)] = True
        if sum(recurrent) == sum(new_recurrent):
            break
        recurrent = new_recurrent
    # Iterate over the loops...
    result = 1
    while sum(recurrent):
        # Step 2: Find a loop of recurrent states.
        loop = [recurrent.index(True)]
        node = f(loop[0])
        while node != loop[0]:
            loop.append(node)
            node = f(node)
        # Step 3: For each state in the loop, find the count of tree colorings.
        reds = [1 for node in loop]
        blacks = [1 for node in loop]
        for i in range(len(loop)):
            child = first_child(loop[i])
            if child in loop:
                child = second_child(loop[i])
            if child == -1:
                continue
            child_configs = count_configs(child)
            reds[i] = child_configs[1] % mod
            blacks[i] = sum(child_configs) % mod
        # Step 4: Travel around loop, counting configs as we go
        ends = [reds[0], 0]  # No. where last node is red/black. 1st assume red
        for i in range(1, len(loop)):
            ends = [(ends[1] * reds[i]) % mod, (sum(ends) * blacks[i]) % mod]
        loop_count = ends[1]  # If first is red, last has to be black
        ends = [0, blacks[0]]  # 2nd assume black
        for i in range(1, len(loop)):
            ends = [(ends[1] * reds[i]) % mod, (sum(ends) * blacks[i]) % mod]
        loop_count += sum(ends)  # If first is red, last can be either color
        # Step 5: Multiply the result, and make sure we don't re-do this loop
        result *= loop_count
        result %= mod
        for node in loop:
            recurrent[node] = False
    return result

if __name__ == "__main__":
    start = time()
    peresult(703, solve(), time() - start)
