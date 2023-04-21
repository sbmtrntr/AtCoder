N, L = map(int, input().split())
MOD = 10**9 + 7

dp = [0 for _ in range(N+1)]

dp[0] = 1

for i in range(1, N+1):
    if i - L >= 0:
        dp[i] = (dp[i-1] + dp[i-L]) % MOD
    else:
        dp[i] = dp[i-1]

print(dp[N])
