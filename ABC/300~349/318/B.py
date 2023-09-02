N = int(input())
masu = [[0]*(101) for _ in range(101)]

for i in range(N):
    a, b, c, d = map(int,input().split())
    for i in range(c, d):
        for j in range(a, b):
            masu[i][j] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if masu[i][j] != 0:
            ans += 1
print(ans)