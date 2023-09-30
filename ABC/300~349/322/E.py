N, K, P = map(int, input().split())
C, A = [], []
for i in range(N):
    temp = list(map(int, input().split()))
    C.append(temp[0])
    A.append(temp[1:])
INF = 10**10
dp = [[INF]*2**K for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1): # i個目の企画案
    for j in range(2**K): # j個目の集合
        dp[i][j] = min(dp[i][j], dp[i-1][j])

        parameters = [0]*K
        for k in range(K):
            if j & (1 << k):
                parameters[k] += A[i][k]

        v = 0
        for k in range(N):
            if parameters[k] >= P:
                v += 2**k
        
        dp[i][v] = min(dp[i][v], dp[i-1][j] + C[i])