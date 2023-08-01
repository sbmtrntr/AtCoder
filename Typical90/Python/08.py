N = int(input())
S = input()
mod = 10**9 + 7
dp = [[0]*8 for _ in range(N+1)]
T = "atcoder"

dp[0][0] = 1

for i in range(N):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod

        if j != 7 and S[i] == T[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod

print(dp[N][7])