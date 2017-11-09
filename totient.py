from factorfns import primefactors

def totient(num):
        factors = primefactors(num)
        result = num
        for factor in factors:
                result = result * (factor - 1) // factor
        return result
