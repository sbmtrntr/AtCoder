from collections import defaultdict
N = int(input())
mx = 1002
masu = [[0]*mx for _ in range(mx)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    masu[lx][ly] += 1
    masu[rx][ry] += 1
    masu[lx][ry] -= 1
    masu[rx][ly] -= 1

for i in range(mx-1):
    for j in range(mx-1):
        masu[i][j+1] += masu[i][j]

for i in range(mx-1):
    for j in range(mx-1):
        masu[i+1][j] += masu[i][j]

ans = defaultdict(int)

for i in range(mx):
    for j in range(mx):
        ans[masu[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])