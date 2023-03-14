N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

dp = [0]*(X+1)

for i in range(M):
    dp[B[i]] = -1

dp[0] = 1

for i in range(X+1):
    if dp[i] == 1:
        for j in range(N):
            try:
                if dp[i+A[j]] != -1:
                    dp[i+A[j]] = 1
            except:
                continue


if dp[X] == 1:
    print('Yes')
else:
    print('No')