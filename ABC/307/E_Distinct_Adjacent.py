N, M = map(int, input().split())
p = 998244353

print((pow(M - 1, N, p) + pow(-1, N, p) * (M - 1)) % p)