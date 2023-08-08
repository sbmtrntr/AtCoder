N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [0]*N
dp[1] = A[0]
for i in range(N-2):
    dp[i+2] = min(dp[i+1] + A[i+1], dp[i] + B[i])


idx = N-1
ans = [idx+1]
while idx != 0:
    if dp[idx] - dp[idx-1] == A[idx-1]:
        idx -= 1
        ans.append(idx+1)
    else:
        idx -= 2
        ans.append(idx+1)

print(len(ans))
print(*ans[::-1])