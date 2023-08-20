import sys
sys.setrecursionlimit(10**8)

N = int(input())
C, P = [], []
for i in range(N):
    temp = list(map(int, input().split()))
    C.append(temp[0])
    P.append(temp[1:])
ans = []
seen = [False]*(N+1)
def dfs(x):
    seen[x] = True
    for y in P[x-1]:
        if seen[y]:
            continue
        dfs(y)
        ans.append(y)

dfs(1)
print(*ans)