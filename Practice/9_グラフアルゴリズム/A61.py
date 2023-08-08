from collections import defaultdict
N, M = map(int, input().split())
graph = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for i in range(1, N+1):
    if i not in graph:
        print(str(i) + ": {}")
    else:
        print(f"{i}: {graph[i]}")