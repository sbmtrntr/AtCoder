import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict
N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

seen = [False]*(N+1)

def dfs(x):
    if x == N:
        print(*ans)
        exit()
    seen[x] = True
    for y in graph[x]:
        if seen[y]:
            continue
        ans.append(y)
        dfs(y)
        ans.pop()

ans = [1]
dfs(1)