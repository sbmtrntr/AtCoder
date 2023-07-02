import sys
sys.setrecursionlimit(10**7)
H, W = map(int, input().split())
S = []
for i in range(H):
    temp = list(input())
    S.append(temp)
snuke = "snuke"
def dfs(x, y, cnt):
    # ゴールに辿り着ければ終了
    if x == H-1 and y == W-1:
        print('Yes')
        exit()

    # 上下左右への移動パターンで再起していく
    if x+1 < H and S[x+1][y] == snuke[(cnt+1) % 5]:
        S[x+1][y] = '#'
        dfs(x+1, y, cnt+1)
    if 0 <= x-1 and S[x-1][y] == snuke[(cnt+1) % 5]:
        S[x-1][y] = '#'
        dfs(x-1, y, cnt+1)
    if y+1 < W and S[x][y+1] == snuke[(cnt+1) % 5]:
        S[x][y+1] = '#'
        dfs(x, y+1, cnt+1)
    if 0 <= y-1 and S[x][y-1] == snuke[(cnt+1) % 5]:
        S[x][y-1] = '#'
        dfs(x, y-1, cnt+1)

dfs(0, 0, 0)
print('No')