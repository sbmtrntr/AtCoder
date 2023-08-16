from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

que = deque([(sy, sx)])
c[sy][sx] = 0

while que:
    y, x = que.popleft()
    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C and c[ny][nx] == '.':
            c[ny][nx] = c[y][x] + 1
            que.append((ny, nx))

print(c[gy][gx])