N, M, K = map(int, input().split())

MOD = 998244353

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

dp[0][0] = 1

#行が項数、列が総和が何通りあるか
for i in range(N):
    for j in range(K):
        for k in range(1, M+1):
            if j + k <= K:
                dp[i+1][j+k] += dp[i][j]


print(sum(dp[N]) % MOD)