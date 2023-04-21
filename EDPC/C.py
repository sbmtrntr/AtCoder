N = int(input())

dp = [[0]*N for _ in range(3)]

a, b, c = map(int, input().split())

dp[0][0] = a
dp[1][0] = b
dp[2][0] = c
for i in range(1, N):
    a, b, c = map(int, input().split())
    dp[0][i] = max(dp[1][i-1] + a, dp[2][i-1] + a)
    dp[1][i] = max(dp[0][i-1] + b, dp[2][i-1] + b)
    dp[2][i] = max(dp[0][i-1] + c, dp[1][i-1] + c)

print(max(dp[1][-1], dp[0][-1], dp[2][-1]))