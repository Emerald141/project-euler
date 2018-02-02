def numassemble(*digits):
        result = 0
        for x in range(len(digits)):
                result *= 10
                result += digits[x]
        return result
