N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
mod = 998244353

dp[0][0] = 1
dp[0][1] = 1

for i in range(1, N):
    for pre in range(2):
        for nxt in range(2):
            if AB[i-1][pre] != AB[i][nxt]:
                dp[i][nxt] += dp[i-1][pre]
    dp[i][0] %= mod
    dp[i][1] %= mod

print((dp[N-1][0] + dp[N-1][1]) % mod)