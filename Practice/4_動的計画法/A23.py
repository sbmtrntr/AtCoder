from itertools import product
N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
ans = 11

for pro in product((0, 1), repeat=M):
    ok = [0]*N
    for i in range(M):
        if pro[i] == 0:
            continue
        for j in range(N):
            ok[j] = max(ok[j], A[i][j])
        
    if sum(ok) == N:
        ans = min(ans, sum(pro))

if ans == 11:
    print(-1)
else:
    print(ans)