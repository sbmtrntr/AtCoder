from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N, M  = map(int, input().split())
Graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    Graph[u].append(v)
    Graph[v].append(u)

if N != M + 1:
    exit(print('No'))

for v in Graph.values():
    if len(v) > 2:
        exit(print('No'))

seen = [False]*(N+1)

def dfs(num):
    seen[num] = True
    for to in Graph[num]:
        if seen[to]:
            continue
        else:
            dfs(to)

dfs(1)

if sum(seen) == N:
    print('Yes')
else:
    print('No')