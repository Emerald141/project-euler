# The four adjacent digits in the 1000-digit number stored in the text file
# that have the greatest product are 9 * 9 * 8 * 9 = 5832.
#
# Find the thirteen adjacent digits in the 1000-digit number that have
# the greatest product. What is the value of this product?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    file = open('../textfiles/p008_thousanddigits.txt')
    number_string = file.read().replace('\n', '')
    largest_mult = 0
    current_mult = 1
    mult_terms = 0
    for index in range(len(number_string)):
        if number_string[index] == '0':
            current_mult = 1
            mult_terms = 0
        else:
            current_mult *= int(number_string[index])
            if mult_terms == 13:
                current_mult //= int(number_string[index - 13])
                if current_mult > largest_mult:
                    largest_mult = current_mult
            else:
                mult_terms += 1
    return largest_mult

if __name__ == "__main__":
    start = time()
    peresult(8, solve(), time() - start)
