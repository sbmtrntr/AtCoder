H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

alpha = "abcdefghijklmnopqrstuvwxyz"
col = [[0]*26 for _ in range(H)]
row = [[0]*26 for _ in range(W)]

for i in range(H):
    for j in range(W):
        k = ord(c[i][j]) - ord('a')
        col[i][k] += 1
        row[j][k] += 1

