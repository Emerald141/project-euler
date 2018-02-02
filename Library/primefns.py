def isprime(num):
    if num < 2:
        return False
    for factor in range(2, int(num ** .5) + 1):
        if num % factor == 0:
            return False
    return True

def primesbelow(num):
    bignum = 0
    if num > 10 ** 7:
        bignum = num
        num = 10 ** 7
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
    if bignum != 0:
        for tenmilmult in range(10 ** 7, bignum, 10 ** 7):
            cap = min(bignum, tenmilmult + 10 ** 7) - tenmilmult
            sieve = [True for x in range(cap)]
            for p in result:
                if p ** 2 >= cap + tenmilmult:
                    break
                multiple = -1 - ((tenmilmult - 1) % p) + p
                while multiple < cap:
                    sieve[multiple] = False
                    multiple += p
            for x in range(len(sieve)):
                if sieve[x]:
                    result.append(x + tenmilmult)
    return result

def primeabove(num):
    testnum = (num + 1) // 2 * 2 + 1
    while not isprime(testnum):
        testnum += 2
    return testnum
