H, W = map(int, input().split())
S = [input() for _ in range(H)]
a, b, c, d = 1000, 1000, -1, -1
for i in range(H):
    flag = False
    for j in range(W):
        if not flag and S[i][j] == "#":
            a = min(a, i)
            b = min(b, j)
            c = max(c, i)
            d = max(d, j)

for i in range(H):
    for j in range(W):
        if a <= i <= c and b <= j <= d and S[i][j] == ".":
            print(i+1, j+1)