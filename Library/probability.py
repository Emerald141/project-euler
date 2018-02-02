def factorial(num):
        result = 1
        while num > 1:
                result *= num
                num -= 1
        return result

def choose(largenum, smallnum):
        return factorial(largenum) // factorial(smallnum) // factorial(largenum - smallnum)

def chooseMulti(largenum, *smallnums):
        result = factorial(largenum)
        for smallnum in smallnums:
                result //= factorial(smallnum)
        result //= factorial(largenum - sum(smallnums))
        return result
