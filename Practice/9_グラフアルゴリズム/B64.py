import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # 初期化
    visited = [False] * N
    distance = [10**10] * N
    distance[start] = 0
    pq = [(0, start)]

    # ダイクストラ法
    while pq:
        # 未処理の中で最小の距離を持つ頂点を取り出す
        dist, u = heapq.heappop(pq)
        if visited[u]:
            continue

        # 訪問済みにする
        visited[u] = True

        # uから到達可能な頂点の距離を更新する
        for v, weight in graph[u]:
            if not visited[v]:
                new_distance = distance[u] + weight
                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(pq, (new_distance, v))
                    ans.append(v+1)

    return distance

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

start = 0
ans = [1]
distance = dijkstra(graph, start)
print(*ans)