N, S = map(int,input().split())
A = list(map(int,input().split()))

dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(S):
        if dp[i][j]:
            dp[i+1][j] = True
        if dp[i][j] and j + A[i] <= S:
            dp[i+1][j+A[i]] = True

if dp[N][S]:
    idx = N
    ans = []
    while idx != 0:
        for i in range(S):
            if 0 <= S - A[i] <= S and dp[idx-1][S-A[i]]:
                ans.append(i)
                idx -= 1

else:
    print(-1)