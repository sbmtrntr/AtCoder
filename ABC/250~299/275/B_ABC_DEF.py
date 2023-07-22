A, B, C, D, E, F = map(int, input().split())
MOD = 998244353
A %= MOD
B %= MOD
C %= MOD
D %= MOD
E %= MOD
F %= MOD
ans = (A * B) % MOD * C % MOD
ans -= (D * E) % MOD * F % MOD
print(ans % MOD)