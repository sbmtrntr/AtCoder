N = int(input())
masu = [[0]*10 for _ in range(10)]

for i in range(N):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    masu[x][y] += 1

for i in range(10):
    for j in range(9):
        masu[i][j+1] += masu[i][j]
    
for j in range(10):
    for i in range(9):
        masu[i+1][j] += masu[i][j]

Q = int(input())

for _ in range(Q):
    a, b, c, d = map(int,input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    print(masu[c+1][d+1] - masu[c+1][b] - masu[a][d+1] + masu[a][b])