MOD = 10**9+7

S = input()
N = len(S)
T = "chokudai"
ans = 0

dp = [[0 for _ in range(N+1)] for _ in range(9)]

#1行目を全て1で初期化
for i in range(N+1):
    dp[0][i] = 1

for i in range(8): #iは行番号
    for j in range(N): #jは列番号
        if S[j] != T[i]:
            dp[i+1][j+1] = dp[i+1][j]
        else:
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j] % MOD

print(dp[8][N])
