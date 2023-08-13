N = int(input())
T, D = [0]*N, [0]*N
for i in range(N):
    T[i], D[i] = map(int, input().split())

dp = [[0]*11 for _ in range(N+1)]

for i in range(N):
    for j in range(11):
        if j == T[i] and j + T[i] <= 10:
            dp[i+1][j+T[i]] = max(dp[i+1][j] + D[i], dp[i+1][j+T[i]])
        
        if dp[i][j] != 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp)