N = int(input())
XY = []
for i in range(N):
    hoge = tuple(map(int, input().split()))
    XY.append(hoge)

# 0 = 元気で食べる 1 = 元気で食べない 2 = 病気で食べる 3 = 病気で食べない
dp = [[0, 0, 0, 0] for _ in range(N+1)]

for i in range(N):
    # 解毒剤入り
    if XY[i][0] == 0:
        dp[i+1][0] = max(dp[i]) + XY[i][1]
        dp[i+1][1] = max(dp[i][0], dp[i][1])
        dp[i+1][3] = max(dp[i][2], dp[i][3])

    # 毒入り
    else:
        dp[i+1][1] = max(dp[i][0], dp[i][1])
        dp[i+1][2] = max(dp[i][0], dp[i][1]) + XY[i][1]
        dp[i+1][3] = max(dp[i][2], dp[i][3])

print(max(dp[-1]))