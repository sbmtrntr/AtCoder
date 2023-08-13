N = int(input())
L = 10
masu = [[0]*L for _ in range(L)]

for i in range(N):
    x, y = map(int,input().split())
    masu[x][y] += 1

for i in range(L):
    for j in range(L-1):
        masu[i][j+1] += masu[i][j]
    
for j in range(L):
    for i in range(L-1):
        masu[i+1][j] += masu[i][j]

Q = int(input())

for _ in range(Q):
    a, b, c, d = map(int,input().split())
    print(masu[c][d] - masu[c][b-1] - masu[a-1][d] + masu[a-1][b-1])