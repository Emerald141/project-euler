from primefns import isprime

def factorcount(num):
        result = 2
        for factor in range(2, int(num ** .5) + 1):
                if num % factor == 0:
                        result += 2
        if int(num ** .5) ** 2 == num:
                result -= 1
        return result

def factorsum(num, proper=False):
        result = 1 + num
        if proper:
                result = 1
        for factor in range(2, int(num ** .5) + 1):
                if num % factor == 0:
                        result += factor + (num // factor)
        if int(num ** .5) ** 2 == num:
                result -= int(num ** .5)
        return result

def factorization(num):
        result = []
        iterator = 2
        while num > 1:
                if isprime(iterator):
                        while num % iterator == 0:
                                result.append(iterator)
                                num //= iterator
                iterator += 1
        result.sort()
        return result

def factorizationpow(num):
        result = dict()
        iterator = 2
        while num > 1:
                if isprime(iterator):
                        power = 0
                        while num % iterator == 0:
                                num //= iterator
                                power += 1
                                result[iterator] = power
                iterator += 1
        return result

def primefactors(num):
        result = []
        iterator = 2
        while num > 1:
                if isprime(iterator):
                        if num % iterator == 0:
                                result.append(iterator)
                        while num % iterator == 0:
                                num //= iterator
                iterator += 1
        return result
