N = int(input())

A = []

for i in range(N):
    A.append(list(input()))

ans = "0"

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, -1, 0, 1, -1, 0, 1]

for i in range(N):
    for j in range(N):
        for d in range(8):
            temp = ""
            for k in range(N):
                x = i + dx[d] * k
                y = j + dy[d] * k
                temp += A[x%N][y%N]
            ans = max(ans, temp)

print(ans)


