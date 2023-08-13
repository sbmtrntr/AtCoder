N = int(input())
L = 10
masu = [[0]*(L) for _ in range(L)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    masu[A][B] += 1
    masu[A][D] -= 1
    masu[C][B] -= 1
    masu[C][D] += 1

for i in range(L):
    for j in range(L-1):
        masu[i][j+1] += masu[i][j]

for j in range(L):
    for i in range(L-1):
        masu[i+1][j] += masu[i][j]

ans = 0
for i in range(L):
    for j in range(L):
        if masu[i][j] >= 1:
            ans += 1

print(ans)