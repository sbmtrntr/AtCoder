N, W = map(int, input().split())
w, v = [0]*N, [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        if dp[i][j] != -1 and j+w[i] <= W:
                dp[i+1][j+w[i]] = max(dp[i][j+w[i]], dp[i][j] + v[i])

        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(max(dp[N]))