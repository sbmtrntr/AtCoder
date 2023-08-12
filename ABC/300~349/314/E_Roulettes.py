N, M = map(int, input().split())
C, P, S = [], [], []

for _ in range(N):
    li = list(map(int, input().split()))
    C.append(li[0])
    P.append(li[1])
    S.append(li[2:])

def expected_cost(N, M, P, S, C):
    # 初期化
    INF = float('inf')
    dp = [[INF] * (M+1) for _ in range(N+1)]
    dp[0][0] = 0

    # DPテーブル更新
    for i in range(1, N+1):
        for j in range(M+1):
            for k in range(P[i-1]):
                if j - S[i-1][k] >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j - S[i-1][k]] + C[i-1])

    # 期待値計算
    total_cost = 0
    total_prob = 0
    for j in range(M+1):
        if dp[N][j] != INF and M <= j:
            total_cost += dp[N][j]
            total_prob += 1

    if total_prob == 0:
        return "impossible"
    else:
        expected_value = total_cost / total_prob
        return expected_value

result = expected_cost(N, M, P, S, C)
print(result)