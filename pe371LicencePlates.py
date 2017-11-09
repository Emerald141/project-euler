##Oregon licence plates consist of three letters followed by a
##three digit number (each digit can be from [0..9]).
##While driving to work Seth plays the following game:
##Whenever the numbers of two licence plates seen on his trip
##add to 1000 that's a win.
##
##E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too.
##(as long as he sees them in the same trip).
##
##Find the expected number of plates he needs to see for a win.
##Give your answer rounded to 8 decimal places behind the decimal point.
##
##Note: We assume that each licence plate seen is equally likely to have
##any three digit number on it.

from time import time
from peresult import peresult

def pe371():
        start = time()
        oldInstances = [[0, 0] for x in range(500)]
        oldInstances[0][0] = 1
        weightedCompletes = 0
        totalInstances = 1
        turn = 0
        oldresult = 1 #only so that it won't == 0 at first
        result = 0
        while oldresult != result or turn < 2:
                oldresult = result
                turn += 1
                weightedCompletes *= 1000
                totalInstances *= 1000
                newInstances = [[0, 0] for x in range(500)]
                for ind in range(len(oldInstances)):
                        if oldInstances[ind][0] == 0:
                                break
                        #Instances without 500 plate
                        multer = oldInstances[ind][0]
                        newInstances[ind][0] += multer * (ind + 1)
                        newInstances[ind][1] += multer
                        newInstances[ind+1][0] += multer * (998 - 2 * ind)
                        weightedCompletes += multer * ind * turn
                        #Instances with 500 plate
                        multer = oldInstances[ind][1]
                        newInstances[ind][1] += multer * (ind + 1)
                        newInstances[ind+1][1] += multer * (998 - 2 * ind)
                        weightedCompletes += multer * (ind + 1) * turn
                oldInstances = newInstances
                if totalInstances != 0:
                        result = weightedCompletes / totalInstances
                result *= 10 ** 12
                result = int(result)
                result /= 10 ** 12
        result *= 10 ** 9
        result = round(result, -1)
        result /= 10 ** 9
        peresult(371, result, time() - start)

if __name__ == "__main__":
        pe371()
