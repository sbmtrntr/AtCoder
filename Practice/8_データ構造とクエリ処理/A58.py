N, Q = map(int, input().split())
A = [0]*N

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A[q[1]-1] = q[2]
        