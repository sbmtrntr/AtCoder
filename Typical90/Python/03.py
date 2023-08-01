from collections import defaultdict, deque
N = int(input())
Graph = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

def bfs(st):
    queue = deque([st])
    dist = [-1]*N
    dist[st] = 0
    while queue:
        v = queue.popleft()
        for i in Graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                queue.append(i)
    return dist

dist = bfs(0)

idx = -1
mx = 0
for i in range(N):
    if mx < dist[i]:
        idx = i
        mx = dist[i]

dist = bfs(idx)

print(max(dist) + 1)