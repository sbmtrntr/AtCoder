L, N, S = map(int, input().split())
Y, X = [0]*N, [0]*N
for i in range(N):
    Y[i], X[i] = map(int, input().split())
P = [[0]*L for _ in range(L)]
