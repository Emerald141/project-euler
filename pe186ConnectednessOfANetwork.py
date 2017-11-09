##Here are the records from a busy telephone system with one million users:
##
##RecNr	Caller	Called
##1	200007	100053
##2	600183	500439
##3	600863	701497
##...	...	...
##The telephone number of the caller and the called number in record n
##are Caller(n) = S_(2n-1) and Called(n) = S_(2n) where S_1,2,3,... come
##from the "Lagged Fibonacci Generator":
##
##For 1 ≤ k ≤ 55, S_k = [100003 - 200003k + 300007k^3] (modulo 1000000)
##For 56 ≤ k, S_k = [S_(k-24) + S_(k-55)] (modulo 1000000)
##
##If Caller(n) = Called(n) then the user is assumed to have misdialled
##and the call fails; otherwise the call is successful.
##
##From the start of the records, we say that any pair of users X and Y
##are friends if X calls Y or vice-versa. Similarly, X is a friend of a
##friend of Z if X is a friend of Y and Y is a friend of Z; and so on for
##longer chains.
##
##The Prime Minister's phone number is 524287. After how many successful
##calls, not counting misdials, will 99% of the users (including the PM)
##be a friend, or a friend of a friend etc., of the Prime Minister?

from time import time
from peresult import peresult

mod = 10 ** 6

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LaggedFiboGen:
    def __init__(self):
        #self.rear = Node(1) #TEMPORARY
        self.rear = Node((100003 - 200003 + 300007) % mod)
        tempFront = self.rear
        for k in range(2, 56):
            #tempFront.next = Node(k) #TEMPORARY
            tempFront.next = Node((100003 - (200003*k) + (300007*k**3)) % mod)
            tempFront = tempFront.next
        self.mid = self.rear
        for x in range(31):
            self.mid = self.mid.next
        self.front = tempFront
    def next(self):
        self.front.next = Node((self.rear.value + self.mid.value) % mod)
        self.front = self.front.next
        poppedValue = self.rear.value
        temp = self.rear
        self.rear = self.rear.next
        temp.next = None
        self.mid = self.mid.next
        return poppedValue

def pe186():
    start = time()
    generator = LaggedFiboGen()
    #Representing the network as a set of trees.
    #Index 0 = number of nodes in tree with this node as the root
    #Index 1 = height of tree with this node as the root
    #Index 2 = parent of this node (or -1 if no parent)
    network = [[1, 0, -1] for x in range(mod)]
    pmroot = 524287
    callcount = 0
    while network[pmroot][0] < mod * .99:
        left = generator.next()
        right = generator.next()
        if left == right: #misdial
            continue
        callcount += 1
        while network[left][2] != -1:
            left = network[left][2]
        while network[right][2] != -1:
            right = network[right][2]
        if left == right: #already friends
            continue
        if network[left][1] < network[right][1]: #left tree shorter
            network[left][2] = right #left's new parent is right
            network[right][0] += network[left][0] #new number of children
            if left == pmroot:
                pmroot = right
        else:
            network[right][2] = left #right's new parent is left
            network[left][0] += network[right][0] #new number of children
            if network[left][1] == network[right][1]: #if same height
                network[left][1] += 1 #no option but to increase height
            if right == pmroot:
                pmroot = left
    peresult(186, callcount, time() - start)

if __name__ == "__main__":
    pe186()
