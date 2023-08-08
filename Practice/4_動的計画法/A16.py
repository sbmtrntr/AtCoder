N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [0]*N
dp[1] = A[0]
for i in range(N-2):
    dp[i+2] = min(dp[i+1] + A[i+1], dp[i] + B[i])

print(dp[-1])