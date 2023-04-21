import itertools

N, M = map(int, input().split())

A, B = [[False] * N for _ in range(N)], [[False] * N for _ in range(N)]

for i in range(M):
    i, j = map(int, input().split())
    A[i-1][j-1] = A[j-1][i-1] = True

for i in range(M):
    i, j = map(int, input().split())
    B[i-1][j-1] = B[j-1][i-1] = True

ans = False
for p in itertools.permutations(range(N)):
    ok = True
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[p[i]][p[j]]:
                ok = False
    
    if ok:
        ans = True

print('Yes' if ans else 'No')