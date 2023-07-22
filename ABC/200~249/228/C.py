N, K = map(int, input().split())
P = []
for i in range(N):
    temp = list(map(int, input().split()))
    P.append(temp)

P_sum = [sum(P[i]) for i in range(N)]
ans = [False]*N
Q = sorted(P_sum, reverse=True)

juni = {}
for i in range(N):
    juni[Q[i]] = i + 1

for i in range(N):
    if juni[P_sum[i]] <= K:
        ans[i] = True
        continue
    if Q[K-1] <= P_sum[i] + 300:
        ans[i] = True

for i in ans:
    if i:
        print('Yes')
    else:
        print('No')
    