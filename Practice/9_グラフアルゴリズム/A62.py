from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

seen = [False]*N

def dfs(x):
    seen[x] = True
    for y in graph[x]:
        if not seen[y]:
            dfs(y)

dfs(0)

print("The graph is connected.") if sum(seen) == N else print("The graph is not connected.")