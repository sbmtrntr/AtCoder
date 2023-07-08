from collections import defaultdict, deque
N1, N2, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(u, hoge):
    queue = deque([u])
    d = [-1] * (hoge+1) # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if d[i] == -1:
                d[i] = d[v] + 1
                queue.append(i)
    return d

ans = max(bfs(1, N1))
ans += max(bfs(N1+N2, N1+N2))
print(ans+1)