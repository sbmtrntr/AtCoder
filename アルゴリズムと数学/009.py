n, s = map(int, input().split())

a = list(map(int, input().split()))

dp = [[0]*(s+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(s+1):
        if dp[i][j] == 1:
            dp[i+1][j] = 1
            if j + a[i] <= s:
                dp[i+1][j + a[i]] = 1

if dp[-1][-1] == 1:
    print("Yes")
else:
    print("No")

print(*dp, sep='\n')