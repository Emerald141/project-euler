# Let a_i be the sequence defined by a_i=153^i mod 10,000,019 for i >= 1.
#
# The first terms of $a_i$ are:
# 153, 23409, 3581577, 7980255, 976697, 9434375, ...
#
# Consider the subsequences consisting of 4 terms in ascending order.
# For the part of the sequence shown above, these are:
# 153, 23409, 3581577, 7980255
# 153, 23409, 3581577, 9434375
# 153, 23409, 7980255, 9434375
# 153, 23409, 976697, 9434375
# 153, 3581577, 7980255, 9434375 and
# 23409, 3581577, 7980255, 9434375.
#
# Define S(n) to be the sum of the terms for all such subsequences within the
# first n terms of a_i. Thus S(6)=94513710.
# You are given that S(100)=4465488724217.
#
# Find S(10^6) modulo 1,000,000,007.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

class Node:
    def __init__(self, parent, value, a2, a3):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value
        self.a2 = a2
        self.a3 = a3
        self.st_size = 1
        self.st_a2 = a2
        self.st_a3 = a3

def solve(n = 10 ** 6):
    result = 0
    a2 = [0 for x in range(n)]
    a3 = [0 for x in range(n)]
    key = 153
    tree = Node(None, key, 0, 0)
    for i in range(1, n):
        key = key * 153 % 10000019
        new_a2, new_a3, new_a4 = 0, 0, 0
        node = tree
        while True:
            if key < node.value:
                if node.left == None:
                    node.left = Node(node, key, new_a2, new_a3)
                    break
                node = node.left
            else:  # We won't have any duplicate values in this problem.
                new_a2 += 1
                new_a3 += node.a2
                new_a4 += node.a3
                if node.left:
                    new_a2 += node.left.st_size
                    new_a3 += node.left.st_a2
                    new_a4 += node.left.st_a3
                if node.right == None:
                    node.right = Node(node, key, new_a2, new_a3)
                    break
                node = node.right
        while node:
            node.st_size += 1
            node.st_a2 += new_a2
            node.st_a3 += new_a3
            node = node.parent
        a2[i] = new_a2
        a3[i] = new_a3
        result += new_a4 * key
        result %= 1000000007
    # And now we go back down.
    tree = Node(None, key, 0, 0)
    inverse = pow(153, 10000017, 10000019)
    for i in range(n-2, -1, -1):
        key = key * inverse % 10000019
        new_d2, new_d3, new_d4 = 0, 0, 0
        node = tree
        while True:
            if key < node.value:
                new_d2 += 1
                new_d3 += node.a2
                new_d4 += node.a3
                if node.right:
                    new_d2 += node.right.st_size
                    new_d3 += node.right.st_a2
                    new_d4 += node.right.st_a3
                if node.left == None:
                    node.left = Node(node, key, new_d2, new_d3)
                    break
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(node, key, new_d2, new_d3)
                    break
                node = node.right
        while node:
            node.st_size += 1
            node.st_a2 += new_d2
            node.st_a3 += new_d3
            node = node.parent
        result += new_d2 * a3[i] * key
        result += new_d3 * a2[i] * key
        result += new_d4 * key
        result %= 1000000007
    return result

if __name__ == "__main__":
    start = time()
    peresult(733, solve(), time() - start)
