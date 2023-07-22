from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
Graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

seen = [False]*(N+1)
ans = 0
def dfs(num):
    global ans, seen
    seen[num] = True
    for to in Graph[num]:
        if seen[to]:
            ans += 1

        else:
            dfs(to)


for i in range(1, N+1):
    if seen[i]:
        continue
    seen[i] = True
    dfs(i)

print(ans - M)

