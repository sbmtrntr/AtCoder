N, W = map(int, input().split())

w, v = [0]*N, [0]*N

for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W):
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
        

