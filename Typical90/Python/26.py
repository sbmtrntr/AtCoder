from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

N = int(input())
tree = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

color = [-1]*N

def dfs(pos, col):
    color[pos] = col
    for i in tree[pos]:
        if color[i] == -1:
            dfs(i, 1-col)

dfs(0, 0)
cnt = 0
if sum(color) >= N // 2:
    for i in range(N):
        if cnt < N // 2 and color[i] == 1:
            print(i+1)
            cnt += 1
else:
    for i in range(N):
        if cnt < N // 2 and color[i] == 0:
            print(i+1)
            cnt += 1