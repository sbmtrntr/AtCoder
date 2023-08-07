from collections import deque

H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
sx -= 1; sy -= 1; gx -= 1; gy -= 1
INF = 10**10
maze = [input() for _ in range(H)]
dist = [[INF]*W for _ in range(H)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
dist[sx][sy] = 0
que = deque([(sx, sy)])

while que:
    x, y = que.popleft()
    time = dist[x][y] + 1
    for dx, dy in dir:
        nx = x + dx; ny = y + dy
        while 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == '.' and dist[nx][ny] >= time:
            if dist[nx][ny] == INF:
                que.append((nx, ny))
 
            dist[nx][ny] = time
            nx += dx
            ny += dy

print(dist[gx][gy]-1)