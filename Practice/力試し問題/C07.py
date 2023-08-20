from bisect import bisect
N = int(input())
C = list(map(int, input().split()))
C.sort()
accum = [0]*(N+1)

for i in range(N):
    accum[i+1] = accum[i] + C[i]

Q = int(input())
for _ in range(Q):
    X = int(input())
    print(bisect(accum, X)-1)