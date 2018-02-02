##Each of the six faces on a cube has a different digit (0 to 9)
##written on it; the same is done to a second cube. By placing
##the two cubes side-by-side in different positions we can form
##a variety of 2-digit numbers.
##
##In fact, by carefully choosing the digits on both cubes it is
##possible to display all of the square numbers below one-hundred:
##01, 04, 09, 16, 25, 36, 49, 64, and 81.
##
##For example, one way this can be achieved is by placing
##{0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the
##other cube.
##
##However, for this problem we shall allow the 6 or 9 to be turned
##upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and
##{1, 2, 3, 4, 6, 7} allows for all nine square numbers to be
##displayed; otherwise it would be impossible to obtain 09.
##
##In determining a distinct arrangement we are interested in the
##digits on each cube, not the order.
##
##{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
##{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
##
##But because we are allowing 6 and 9 to be reversed, the two
##distinct sets in the last example both represent the extended
##set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
##
##How many distinct arrangements of the two cubes allow for all
##of the square numbers to be displayed?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        #Die 1 comes preloaded with 0
        #Die 2 comes preloaded with 1
        start = time()
        die1nums = [x for x in range(1, 10)]
        die2nums = [0] + [x for x in range(2, 10)]
        squares = [x ** 2 for x in range(1, 10)]
        result = []
        for ind1_1 in range(5):
                for ind1_2 in range(ind1_1 + 1, 6):
                        for ind1_3 in range(ind1_2 + 1, 7):
                                for ind1_4 in range(ind1_3 + 1, 8):
                                        for ind1_5 in range(ind1_4 + 1, 9):
                                                die1sides = [0, die1nums[ind1_1], die1nums[ind1_2], die1nums[ind1_3], die1nums[ind1_4], die1nums[ind1_5]]
                                                if 6 in die1sides and 9 not in die1sides:
                                                        die1sides.append(9)
                                                if 9 in die1sides and 6 not in die1sides:
                                                        die1sides.append(6)
                                                for ind2_1 in range(5):
                                                        for ind2_2 in range(ind2_1 + 1, 6):
                                                                for ind2_3 in range(ind2_2 + 1, 7):
                                                                        for ind2_4 in range(ind2_3 + 1, 8):
                                                                                for ind2_5 in range(ind2_4 + 1, 9):
                                                                                        die2sides = [1, die2nums[ind2_1], die2nums[ind2_2], die2nums[ind2_3], die2nums[ind2_4], die2nums[ind2_5]]
                                                                                        if 6 in die2sides and 9 not in die2sides:
                                                                                                die2sides.append(9)
                                                                                        if 9 in die2sides and 6 not in die2sides:
                                                                                                die2sides.append(6)
                                                                                        arrangements = []
                                                                                        for side1 in die1sides:
                                                                                                for side2 in die2sides:
                                                                                                        arrangements.append(side1 * 10 + side2)
                                                                                                        arrangements.append(side2 * 10 + side1)
                                                                                        for square in squares:
                                                                                                for arrangement in arrangements:
                                                                                                        if arrangement == square:
                                                                                                                break
                                                                                                else:
                                                                                                        break
                                                                                                continue
                                                                                        else:
                                                                                                if [set(die2sides), set(die1sides)] not in result:
                                                                                                        result.append([set(die1sides), set(die2sides)])
        peresult(90, len(result), time() - start)

if __name__ == "__main__":
        solve()
