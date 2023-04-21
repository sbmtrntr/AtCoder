N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [10**9]*N
dp[0] = 0
dp[1] = abs(H[0]-H[1])

for i in range(2, N):
    for j in range(1, K+1):
        dp[i] = min(dp[i], dp[i-j] + abs(H[i] - H[i-j]))

print(dp[-1])