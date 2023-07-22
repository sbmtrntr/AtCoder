N, M = map(int, input().split())
Ss = [input() for _ in range(N)]
Ts = set()
for _ in range(M):
    Ts.add(input())

ans = 0
for i in range(N):
    if Ss[i][3:6] in Ts:
        ans += 1

print(ans)