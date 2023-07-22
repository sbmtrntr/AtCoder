from collections import defaultdict
N, X = map(int, input().split())
A = [0]*N
B = [0]*N

for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [[False]*(X+1) for _ in range(N)]

for i in range(N):
    for j in range(1, B[i]+1):
        if A[i]*j <= X:
            dp[i][A[i]*j] = True
        for k in range(X+1):
            if i != 0 and dp[i-1][k]:
                dp[i][k] = True
                if k + A[i]*j <= X:
                    dp[i][k + A[i]*j] = True

if dp[-1][-1]:
    print('Yes')
else:
    print('No')