MOD = 10**9 + 7

N = int(input())

C = list(map(int, input().split()))

ans = 1
C.sort()

for i in range(N):
    if C[i] - i > 0:
        ans *= C[i] - i
        ans %= MOD
    else:
        ans = 0

print(ans)