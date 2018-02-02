##If the numbers 1 to 5 are written out in words:
##one, two, three, four, five, then there are
##3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand)
##inclusive were written out in words, how many
##letters would be used?
##
##NOTE: Do not count spaces or hyphens. For example,
##342 (three hundred and forty-two) contains 23 letters
##and 115 (one hundred and fifteen) contains 20 letters.
##The use of "and" when writing out numbers is in
##compliance with British usage.

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

def solve():
        start = time()
        #Ones place digits, repeated except in cases of 11-19:
        onesplace = len("one") + len("two") + len("three")
        onesplace += len("four") + len("five") + len("six")
        onesplace += len("seven") + len("eight") + len("nine")
        onesplace *= 90 #100 minus 10 for elevensplace
        #Last two digits in cases of 10-19:
        elevensplace = len("ten") + len("eleven") + len("twelve")
        elevensplace += 7 * len("teen") + len("thir") + len("four")
        elevensplace += len("fif") + len("six") + len("seven")
        elevensplace += len("eigh") + len("nine")
        elevensplace *= 10
        #Tens place
        tensplace = len("twenty") + len("thirty") + len("forty")
        tensplace += len("fifty") + len("sixty") + len("seventy")
        tensplace += len("eighty") + len("ninety")
        tensplace *= 100 #each word repeated 10x in a row, 10 hundredsets
        #The "and" before the last two digits, unless they're 00
        andsplace = len("and")
        andsplace *= 99 * 9 #99 times per hundredset, 9 hundredsets
        #The hundreds place
        hundredsplace = len("one") + len("two") + len("three")
        hundredsplace += len("four") + len("five") + len("six")
        hundredsplace += len("seven") + len("eight") + len("nine")
        hundredsplace += 9 * len("hundred")
        hundredsplace *= 100 #100 times per hundredset, duh
        #And finally
        thousandsplace = len("onethousand") #remember, no space!
        #Summing it all together:
        result = onesplace + elevensplace + tensplace
        result += andsplace + hundredsplace + thousandsplace
        peresult(17, result, time() - start)

if __name__ == "__main__":
        solve()
