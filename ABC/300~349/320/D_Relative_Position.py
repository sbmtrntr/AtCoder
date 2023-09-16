from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
graph = defaultdict(list)
coord = [[0, 0] for _ in range(N)]
seen = [False]*N

for i in range(M):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, x, y))
    graph[b].append((a, -x, -y))

seen[0] = True

def dfs(u):
    seen[u] = True
    for v, x, y in graph[u]:
        if not seen[v]:
            coord[v][0] = coord[u][0] + x
            coord[v][1] = coord[u][1] + y
            dfs(v)

dfs(0)
for i in range(N):
    if seen[i]:
        print(*coord[i])
    else:
        print('undecidable')