##You are given the following information, but you may prefer
##to do some research for yourself.
##
##1 Jan 1900 was a Monday.
##Thirty days has September,
##April, June and November.
##All the rest have thirty-one,
##Saving February alone,
##Which has twenty-eight, rain or shine.
##And on leap years, twenty-nine.
##
##A leap year occurs on any year evenly divisible by 4, but not
##on a century unless it is divisible by 400.
##How many Sundays fell on the first of the month during the
##twentieth century (1 Jan 1901 to 31 Dec 2000)?

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        daymark = 2 #Jan 1, 1901 was a Monday
        sundaycount = 0
        for year in range(1901, 2001):
                for month in range(1, 13): #1=Jan, 2=Feb, etc.
                        daymark %= 7
                        if daymark == 0:
                                sundaycount += 1
                        if month in [4, 6, 9, 11]:
                                daymark += 30
                        elif month == 2:
                                if year % 4 == 0: #no non-400 100s
                                        daymark += 29
                                else:
                                        daymark += 28
                        else:
                                daymark += 31
        peresult(19, sundaycount, time() - start)
        
if __name__ == "__main__":
        solve()
