N = int(input())
X, Y, Z = [0]*N, [0]*N, [0]*N
for i in range(N):
    X[i], Y[i], Z[i] = map(int, input().split())

victory = (sum(Z)+1) // 2
major = [0]*N

for i in range(N):
    major[i] = max(0, (Y[i] - X[i] + 1)//2)

INF = 10**10
S = sum(Z)
dp = [INF]*(S+1)

for i in range(N):
    for j in range(S):
        dp[j] = min(dp[j], dp[j-major[i]]+)