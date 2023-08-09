N, Q = map(int,input().split())
A = [i for i in range(1, N+1)]

rev = False

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        if rev:
            A[N-(q[1]-1)-1] = q[2]
        else:
            A[q[1]-1] = q[2]
    elif q[0] == 2:
        rev = not rev
    
    else:
        if rev:
            print(A[N-(q[1]-1)-1])
        else:
            print(A[q[1]-1])