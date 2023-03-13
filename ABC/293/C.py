from collections import deque
H, W = map(int, input().split())
A = [
    list(map(int, input().split())) for _ in range(H)
]

sx = 0
sy = 0
Q = deque()
Q.append(sx, sy)
dist = [[-1]*W for _ in range(H)]
dist[0][0] = 0
dirc = [(1, 0), (0, 1)]

while len(Q) > 0:
    y, x = Q.popleft()
    for dy, dx in dirc:
        y2 = y + dy
        x2 = x + dx

        if not (0 <= y2 < H and 0 <= x2 < W):
            continue
