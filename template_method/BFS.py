from collections import deque, defaultdict
graph = defaultdict(list)

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