N, Q = map(int, input().split())

A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

for i in range(Q):
    s, t = map(int, input().split())
    print(A[s-1][t])