N = int(input())
h = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

idx = N-1
ans = [idx+1]
while idx != 0:
    if dp[idx] - dp[idx-1] == abs(h[idx] - h[idx-1]):
        idx -= 1
        ans.append(idx+1)
    else:
        idx -= 2
        ans.append(idx+1)

print(len(ans))
print(*ans[::-1])

