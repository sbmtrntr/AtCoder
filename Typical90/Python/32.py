from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    XY[x-1][y-1] = XY[y-1][x-1] = True

ans = 10**5

for p in permutations(range(N)):
    flag = True
    for i in range(N-1):
        if XY[p[i]][p[i+1]]:
            flag = False
            break
    temp = 0
    if flag:
        for i in range(N):
            temp += A[p[i]][i]
        ans = min(ans, temp)

if ans == 100000:
    print(-1)
else:
    print(ans)
            