##Using network.txt, a 6K text file containing a network with forty vertices,
##and given in matrix form, find the maximum saving which can be achieved by
##removing redundant edges whilst ensuring that the network remains connected.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult
from os import chdir

def solve():
    start = time()
    chdir("textfiles")
    file = open("p107_network.txt")
    #Step 1: Create a formal matrix from the file
    matrix = []
    for line in file:
        matrix.append(line.rstrip().split(','))
    #Step 2: Use the matrix to find a list of all edges and their cost
    edges = []
    oldCost = 0
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            if matrix[row][col] != '-':
                edges.append((int(matrix[row][col]), row, col))
                oldCost += int(matrix[row][col])
    #Step 3: Sort the edges by cost
    edges.sort()
    #Step 4: Set up a list to determine if two nodes are connected
    #Interpret this as a directed graph; -1 means terminal point
    #Any other number means connected to node represented by that number
    connections = [-1 for x in range(40)]
    def areConnected(node1, node2):
        pointer1, pointer2 = node1, node2
        while connections[pointer1] != -1:
            pointer1 = connections[pointer1]
        while connections[pointer2] != -1:
            pointer2 = connections[pointer2]
        if pointer1 == pointer2:
            return True
        #Connect the edges
        connections[pointer1] = pointer2
        return False
    #Step 5: Add the 39 cheapest edges which connect sections of the graph
    newCost = 0
    edgesDrawn = 0
    edgeNum = 0
    while edgesDrawn < 39:
        if not areConnected(edges[edgeNum][1], edges[edgeNum][2]):
            newCost += edges[edgeNum][0]
            edgesDrawn += 1
        edgeNum += 1
    #Step 6: Return the cost of all edges minus the cost of those edges
    result = oldCost - newCost
    peresult(107, result, time() - start)

if __name__ == "__main__":
    solve()
