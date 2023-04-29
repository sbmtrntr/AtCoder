H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

for s in range(H):
    for t in range(W):
        new = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                new[i][j] = A[(i+s)%H][(j+t)%W]
        if new == B:
            exit(print('Yes'))

print('No')
        