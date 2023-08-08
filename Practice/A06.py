N, Q = map(int, input().split())
A = list(map(int, input().split()))
accum = [0]*(N+1)
for i in range(N):
    accum[i+1] = accum[i] + A[i]

for i in range(Q):
    L, R = map(int, input().split())
    print(accum[R] - accum[L-1])