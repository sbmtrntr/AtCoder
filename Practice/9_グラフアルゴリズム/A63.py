from collections import deque, defaultdict
N, M = map(int, input().split())
graph = defaultdict(list)
que = deque([])
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

que.append(0)
dist = [-1]*N
dist[0] = 0

while que:
    x = que.popleft()
    for y in graph[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            que.append(y)

print(*dist)