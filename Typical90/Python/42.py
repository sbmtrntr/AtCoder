K = int(input())
mod = 10**9 + 7

# 各桁の数字の和が9の倍数かつKになるもの
if K % 9 != 0:
    print(0)
else:
    dp = [0]*(K+1)
    dp[0] = 1
    for i in range(1, K+1):
        m = min(i, 9)
        for j in range(1, m+1):
            dp[i] += dp[i-j]
        
        dp[i] %= mod
    print(dp[-1])