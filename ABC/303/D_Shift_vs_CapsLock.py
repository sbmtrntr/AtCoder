X, Y, Z = map(int, input().split())
S = input()
dp = [[0, 0] for _ in range(len(S)+1)]

if S[0] == 'a':
    dp[1][0] = X
    dp[1][1] = Z + Y
else:
    dp[1][0] = Y
    dp[1][1] = Z + X

for i in range(1, len(S)):
    if S[i] == 'a':
        dp[i+1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i+1][1] = min(dp[i][0] + Z + Y,  dp[i][1] + Y)
    else:
        dp[i+1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i+1][1] = min(dp[i][0] + Z + X,  dp[i][1] + X)

print(min(dp[-1][0], dp[-1][1]))