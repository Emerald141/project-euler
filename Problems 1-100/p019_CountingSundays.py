# You are given the following information, but you may prefer
# to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not
# on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
    starting_day = 2  # 1 Jan 1900 was a Monday = 2. Tuesday = 3, etc.
    sunday_count = 0
    for year in range(1900, 2001):
        for month in range(1, 13):  # 1 = Jan, 2 = Feb, etc.
            starting_day %= 7
            if starting_day == 0 and year != 1900:
                sunday_count += 1
            if month in [4, 6, 9, 11]:
                starting_day += 30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    starting_day += 29
                else:
                    starting_day += 28
            else:
                starting_day += 31
    return sunday_count

if __name__ == "__main__":
    start = time()
    peresult(19, solve(), time() - start)
