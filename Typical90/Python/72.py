import sys
sys.setrecursionlimit(10**5)

H, W = map(int, input().split())
c = [input() for _ in range(H)]

dist = [[-1]*W for _ in range(H)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y, cnt):
    if dist[x][y] != -1:
        if cnt - dist[x][y] >= 4:
            return cnt - dist[x][y]
        else:
            return -1
    
    num = -1
    dist[x][y] = cnt
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W and c[nx][ny] == '.':
            num = max(num, dfs(nx, ny, cnt+1))
    dist[x][y] = -1

    return num

ans = -1

for i in range(H):
    for j in range(W):
        if c[i][j] == ".":
            ans = max(ans, dfs(i, j, 0))

print(ans)