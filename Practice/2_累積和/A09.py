H, W, N = map(int, input().split())

masu = [[0]*(W+1) for _ in range(H+1)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    masu[A][B] += 1
    masu[A][D+1] -= 1
    masu[C+1][B] -= 1
    masu[C+1][D+1] += 1

for i in range(H):
    for j in range(W-1):
        masu[i][j+1] += masu[i][j]

for j in range(W):
    for i in range(H-1):
        masu[i+1][j] += masu[i][j]

for i in range(H):
    for j in range(W):
        print(masu[i][j], end=' ')
    print()