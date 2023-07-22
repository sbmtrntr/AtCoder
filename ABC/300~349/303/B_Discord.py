N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]
ans = [set() for _ in range(N)]

for i in range(M):
    for j in range(N):
        if j != 0:
            ans[a[i][j]-1].add(a[i][j-1])
        if j != N-1:
            ans[a[i][j]-1].add(a[i][j+1])

kotae = 0

for a in ans:
    kotae += N - len(a) - 1
print(kotae // 2)