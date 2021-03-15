N = 2021

mod = 1000000007
fact = [1 for x in range(4 * N + 1)]
fact_inv = [1 for x in range(4 * N + 1)]
for x in range(1, 4 * N + 1):
    fact[x] = (fact[x-1] * x) % mod
    fact_inv[x] = pow(fact[x], mod - 2, mod)
result = 0
for n in range(2, N + 1):
    m = (2 * fact[2 * n] ** 2) % mod
    for k in range(1, n + 1):
        term = pow(-1, k)
        term *= fact[n] * fact_inv[k] * fact_inv[n-k]
        term *= 8 * n * pow(4, k, mod)
        term *= fact[4 * n - 3 * k - 1] * fact_inv[4 * n - 4 * k]
        term *= fact[2 * n - 2 * k] ** 2
        m += term
    m %= mod
    result += m
    result %= mod
print(result)