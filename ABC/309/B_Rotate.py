N = int(input())
A = [input() for _ in range(N)]
ans = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0:
            if j == 0:
                ans[i][j] = A[i+1][j]
            else:
                ans[i][j] = A[i][j-1]
        elif i == N-1:
            if j == N-1:
                ans[i][j] = A[i-1][j]
            else:
                ans[i][j] = A[i][j+1]
        elif j == 0:
            ans[i][j] = A[i+1][j]
        elif j == N-1:
            ans[i][j] = A[i-1][j]
        else:
            ans[i][j] = A[i][j]
for i in range(N):
    for j in range(N):
        print(ans[i][j], end='')
    print()