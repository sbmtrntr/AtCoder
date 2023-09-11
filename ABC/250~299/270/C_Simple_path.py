from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
N, X, Y = map(int, input().split())
X -= 1
Y -= 1
graph = defaultdict(list)

for i in range(N-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = []
seen = [False]*N

def dfs(current, parent):
    seen[current] = True
    if current == Y:
        ans.append(Y+1)
        return True
    
    for neighbor in graph[current]:
        if not seen[neighbor] and neighbor != parent:
            if dfs(neighbor, current):
                ans.append(current+1)
                return True
    return False

dfs(X, -1)
print(*ans[::-1])