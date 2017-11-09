def isprime(num):
        if num < 2:
                return False
        for factor in range(2, int(num ** .5) + 1):
                if num % factor == 0:
                        return False
        return True

def primesbelow(num):
        sieve = [False, False] + [True for x in range(2, num)]
        for x in range(2, int((num + 1) ** .5) + 1):
                if sieve[x]:
                        multiple = x ** 2
                        while multiple < len(sieve):
                                sieve[multiple] = False
                                multiple += x
        result = []
        for x in range(len(sieve)):
                if sieve[x]:
                        result.append(x)
        return result

def primeabove(num):
        testnum = (num + 1) // 2 * 2 + 1
        while not isprime(testnum):
                testnum += 2
        return testnum
