##By using each of the digits from the set, {1, 2, 3, 4}, exactly once,
##and making use of the four arithmetic operations (+, −, *, /) and
##brackets/parentheses, it is possible to form different positive integer
##targets.
##
##For example,
##
##8 = (4 * (1 + 3)) / 2
##14 = 4 * (3 + 1 / 2)
##19 = 4 * (2 + 3) − 1
##36 = 3 * 4 * (2 + 1)
##
##Note that concatenations of the digits, like 12 + 34, are not allowed.
##
##Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
##target numbers of which 36 is the maximum, and each of the numbers 1 to 28
##can be obtained before encountering the first non-expressible number.
##
##Find the set of four distinct digits, a < b < c < d, for which the longest
##set of consecutive positive integers, 1 to n, can be obtained, giving your
##answer as a string: abcd.

from time import time
from peresult import peresult

def pe93():
    #Miraculously, this program worked on the first try
    start = time()
    digs = [1, 2, 3, 3] #First value will be [1, 2, 3, 4]
    highestGlobal = 0
    while True:
        #Move to the next value in the synthetic nested for loops
        if digs[3] != 9:
            digs[3] += 1
        else:
            index = 3
            while index >= 0 and digs[index] == 6 + index:
                index -= 1
            if index == -1:
                break
            digs[index] += 1
            while index < 3:
                index += 1
                digs[index] = digs[index - 1] + 1
        #Make a set of all reachable nums
        reached = set()
        #There's almost certainly an easier way to do this but screw it
        permutes = [ [0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], \
                     [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2], \
                     [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0], \
                     [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], \
                     [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1], \
                     [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0] ]
        for permute in permutes:
            these = [ digs[permute[i]] for i in range(4)]
            ops = [0, 0, 0]
            while True:
                if ops[2] != 3:
                    ops[2] += 1
                elif ops[1] != 3:
                    ops[1], ops[2] = ops[1] + 1, 0
                elif ops[0] != 3:
                    ops[0], ops[1], ops[2] = ops[0] + 1, 0, 0
                else:
                    break
                reached.add(op(op(op(these[0], these[1], ops[0]), these[2], ops[1]), these[3], ops[2])) # ((a ~ b) ~ c) ~ d
                reached.add(op(op(these[0], op(these[1], these[2], ops[1]), ops[0]), these[3], ops[2])) # (a ~ (b ~ c)) ~ d
                reached.add(op(op(these[0], these[1], ops[0]), op(these[2], these[3], ops[2]), ops[1])) # (a ~ b) ~ (c ~ d)
                reached.add(op(these[0], op(op(these[1], these[2], ops[1]), these[3], ops[2]), ops[0])) # a ~ ((b ~ c) ~ d)
                reached.add(op(these[0], op(these[1], op(these[2], these[3], ops[2]), ops[1]), ops[0])) # a ~ (b ~ (c ~ d))
        #Find how many consecutive numbers can be reached
        highestLocal = 0
        while highestLocal + 1 in reached:
            highestLocal += 1
        #Check to see if this is a new best digit set
        if highestLocal > highestGlobal:
            highestGlobal = highestLocal
            bestDigits = digs[:]
    result = ""
    for digit in bestDigits:
        result += str(digit)
    peresult(93, result, time() - start)

def op(num1, num2, opID):
    if opID == 0:
        return num1 + num2
    elif opID == 1:
        return num1 - num2
    elif opID == 2:
        return num1 * num2
    elif num2 != 0:
        return num1 / num2
    else:
        return 99999999 #Should make target numbers unreachable by mistake

if __name__ == "__main__":
    pe93()
