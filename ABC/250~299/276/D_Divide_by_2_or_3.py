from math import gcd
N = int(input())
A = list(map(int, input().split()))

gcd_mn = 10**9

for i in range(N):
    for j in range(i+1, N):
        gcd_mn = min(gcd_mn, gcd(A[i], A[j]))

ans = 0
for i in range(N):
    A[i] //= gcd_mn
    while A[i] % 2 == 0:
        A[i] //= 2
        ans += 1
    while A[i] % 3 == 0:
        A[i] //= 3
        ans += 1
    if A[i] != 1:
        exit(print(-1))

print(ans)