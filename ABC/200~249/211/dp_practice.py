MOD = 10**9+7

S = input()
N = len(S)
T = "abc"
ans = 0

dp = [[0 for _ in range(N+1)] for _ in range(4)]
for i in range(N+1):
    dp[0][i] = 1

for i in range(3):
    for j in range(N):
        if S[j] != T[i]:
            dp[i+1][j+1] = dp[i+1][j]
        else:
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j]

print(*dp, sep= "\n")