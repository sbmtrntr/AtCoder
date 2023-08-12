import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # 初期化
    visited = [False] * N
    distance = [[10**10, 0]] * N
    distance[start] = [0, 0]
    pq = [(0, 0, 0)] # 距離, -(木の数), ノード番号

    # ダイクストラ法
    while pq:
        # 未処理の中で最小の距離を持つ頂点を取り出す
        dist, tree, u = heapq.heappop(pq)
        if visited[u]:
            continue

        # 訪問済みにする
        visited[u] = True
        distance[u] = [dist, tree]

        # uから到達可能な頂点の距離を更新する
        for v, w, tr in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (dist + w, tree - tr, v))

    return distance

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))

start = 0
distance = dijkstra(graph, start)

print(distance[-1][0], -distance[-1][1])