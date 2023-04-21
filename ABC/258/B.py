N = int(input())

A = []

for i in range(N):
    A.append(list(input()))

ans = 0

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(j, N+j):
            temp += A[i][k%N]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(j, N+j):
            temp += A[i][(N-1+k)%N]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(j, N+j):
            temp += A[(N-1+k)%N][i]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(j, N+j):
            temp += A[k%N][i]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(i, N+i):
            temp += A[k%N][(j+k)%N]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(i, N+i):
            temp += A[(j+k)%N][k%N]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(i, N+i):
            temp += A[N-1-((j+k)%N)][N-1-(k%N)]
        ans = max(ans, int(temp))

for i in range(N):
    for j in range(N):
        temp = ""
        for k in range(i, N+i):
            temp += A[N-1-(k%N)][N-1-((j+k)%N)]
        ans = max(ans, int(temp))

print(ans)