from collections import defaultdict, deque
N, M = map(int, input().split())
graph = defaultdict(list)
que = deque([])
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

que.append(0)
dist = [10**8]*N
dist[0] = 0

while que:
    x = que.popleft()
    for y, c in graph[x]:
        if dist[y] > dist[x] + c:
            dist[y] = dist[x] + c
            que.append(y)

for i in range(N):
    if dist[i] == 10**8:
        print(-1)
    else:
        print(dist[i])