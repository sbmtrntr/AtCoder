N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7

ans = sum(A)**2

ans %= mod

for i in range(N):
    ans -= A[i] ** 2
    ans %= mod

ans //= 2

print(ans%mod)

