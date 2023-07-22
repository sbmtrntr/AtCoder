N = int(input())

A, P, X = [0]*N, [0]*N, [0]*N

for i in range(N):
    A[i], P[i], X[i] = map(int, input().split())

ans = 10**20
for i in range(N):
    X[i] -= A[i]

for i in range(N):
    if X[i] > 0:
        ans = min(ans, P[i])

if ans == 10**20:
    print(-1)
else:
    print(ans)

 
