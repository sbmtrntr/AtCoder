import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
S = [input() for _ in range(N)]
stop = [[False]*M for _ in range(N)]
through = [[False]*M for _ in range(N)]

def dfs(x, y):
    stop[x][y] = True 
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x, y
        while S[nx+dx][ny+dy] != '#':
            nx += dx
            ny += dy
            through[nx][ny] = True
        if not stop[nx][ny]:
            dfs(nx, ny)

through[1][1] = True
dfs(1, 1)
print(sum(sum(a) for a in through))