from collections import defaultdict
N = int(input())
A = [-1] + list(map(int, input().split()))
graph = defaultdict(int)

for i in range(N-1, 0, -1):
    graph[A[i]] += graph[i+1] + 1

ans = [0]*N

for k, v in graph.items():
    ans[k-1] = v

print(*ans)