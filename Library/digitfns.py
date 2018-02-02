def digitsum(number):
        result = 0
        while number > 0:
                result += number % 10
                number //= 10
        return result

def digitproduct(number):
        result = 1
        while number > 0:
                result *= number % 10
                number //= 10
        return result

def digitcount(number):
        result = 0
        while number > 0:
                result += 1
                number //= 10
        return result
                
