N = int(input())
X, Y, Z = [0]*N, [0]*N, [0]*N
for i in range(N):
    X[i], Y[i], Z[i] = map(int, input().split())

victory = (sum(Z)+1) // 2
major = [0]*N

for i in range(N):
    major[i] = max(0, Y[i] - (X[i] + Y[i])//2)

INF = 10**12
S = sum(Z)+1
dp = [[INF]*(S) for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(S):
        if dp[i][j] != INF and j+Z[i] <= S:
                dp[i+1][j+Z[i]] = min(dp[i][j+Z[i]], dp[i][j] + major[i])

        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

print(min(dp[N][victory:]))