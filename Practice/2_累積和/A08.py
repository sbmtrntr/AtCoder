H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())

accum = [[0]*(W+1) for _ in range(H+1)]

for i in range(H):
    for j in range(W):
        accum[i+1][j+1] = accum[i+1][j] + X[i][j]

for j in range(W):
    for i in range(H):
        accum[i+1][j+1] += accum[i][j+1]

for i in range(Q):
    A, B, C, D = map(int, input().split())
    print(accum[C][D] - accum[A-1][D] - accum[C][B-1] + accum[A-1][B-1])