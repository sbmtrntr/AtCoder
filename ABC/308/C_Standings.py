import decimal
N = int(input())
AB = [list(map(decimal.Decimal, input().split())) for _ in range(N)]
decimal.getcontext().prec = 100
ans = []
for i in range(N):
    score = AB[i][0] / (AB[i][0] + AB[i][1])
    ans.append([score, -(i+1)])
ans.sort(reverse=True)

for i in range(N):
    print(-ans[i][1], end=' ')