from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = 0

def dfs(node):
    visited[node] = True
    max_distance = 0
    
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            distance = weight + dfs(neighbor)
            max_distance = max(max_distance, distance)
    
    visited[node] = False  # バックトラック
    return max_distance

ans = 0
for i in range(N):
    visited = [False] * N
    distance = dfs(i)
    ans = max(ans, distance)
    
print(ans)