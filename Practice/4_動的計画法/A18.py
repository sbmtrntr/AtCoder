N, S = map(int,input().split())
A = list(map(int,input().split()))

dp = [[False]*(S+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        if dp[i][j] and j+A[i] <= S:
            dp[i+1][j+A[i]] = True

        if dp[i][j]:
            dp[i+1][j] = True

print('Yes') if dp[-1][S] else print('No')