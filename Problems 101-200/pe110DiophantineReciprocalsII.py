##In the following equation x, y, and n are positive integers.
##
##1/x + 1/y = 1/n
##
##It can be verified that when n = 1260 there are 113 distinct solutions
##and this is the least value of n for which the total number of distinct
##solutions exceeds one hundred.
##
##What is the least value of n for which the number of distinct solutions
##exceeds four million?

from pe108DiophantineReciprocals import pe108

if __name__ == "__main__":
    solve(110, 4000000)
