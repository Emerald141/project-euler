from itertools import count

cap = 100
primecap = 10

# Step 1: Generate list of prime cubes
sieve = [True for x in range(primecap)]
cubes = []
for i in range(2, primecap):
    if sieve[i]:
        cubes.append(i ** 3)
        for mult in range(i * 2, primecap, i):
            sieve[mult] = False

# Step 2: Run through all combos of cubes
result = cap
for pcount in range(1, len(cubes)):
    indexes = list(range(pcount))
    while True:
        print(indexes)
        term = 1
        for i in indexes:
            term *= cubes[i]
        if term < cap:
            result += cap // term
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
print(result)