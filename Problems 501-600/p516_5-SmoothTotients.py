# 5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
# 5-smooth numbers are also called Hamming numbers.
# Let S(L) be the sum of the numbers n not exceeding L such that Euler's
# totient function φ(n) is a Hamming number.
# S(100)=3728.
# 
# Find S(10^12). Give your answer modulo 2^32.

from itertools import count

cap = 10 ** 12

# Step 1: Generate list of Hamming numbers
hammings = []
for i in count(0):
    a = pow(2, i)
    if a > cap:
        break
    for j in count(0):
        b = a * pow(3, j)
        if b > cap:
            break
        for k in count(0):
            c = b * pow(5, k)
            if c > cap:
                break
            hammings.append(c)
hammings = sorted(hammings)

# Step 2: Which of the numbers that are 1 greater than a Hamming are prime?
primes = []
for h in hammings:
    p = h + 1
    if p > 5:
        # Check to see if p is prime
        for d in range(2, int(p ** .5) + 1):
            if p % d == 0:
                break
        else:
            primes.append(p)
primes.append(cap + 1)  # Safeguard

# Step 3: Run through all combos of primes!
result = sum(hammings)  # for when there are no primes except 2, 3, 5
for pcount in range(1, len(primes)):
    indexes = list(range(pcount))
    while True:
        term = 1
        for i in indexes:
            term *= primes[i]
        if term < cap:
            for h in hammings:
                if term * h < cap:
                    result += term * h
                else:
                    break
            indexes[-1] += 1
        else:
            if indexes[0] + (pcount - 1) == indexes[pcount - 1]:
                # We're done with this number of primes.
                break
            # Advance the last index that isn't sequential with all
            # following indexes.
            for j in range(pcount - 2, -1, -1):
                if indexes[j] + 1 != indexes[j+1]:
                    indexes[j] += 1
                    for k in range(j + 1, pcount):
                        indexes[k] = indexes[k-1] + 1
                    break
print(result % (2 ** 32))