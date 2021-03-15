mod = 1000000007
n = 10 ** 8
m = n
term = pow(2, n * m, mod)
result = term
twopow = pow(4, n * mod - 2 * n, mod)
for k in range(1, n + 1):
    if k % 1000000 == 0:
        print(k)
    term = term * (m - 2 * k + 1) * (m - 2 * k + 2)
    term = term * pow(k, 2 * mod - 4, mod) * twopow
    term %= mod
    result += term
    result %= mod
input(result)