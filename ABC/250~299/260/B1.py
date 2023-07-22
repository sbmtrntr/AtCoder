N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for i in range(N):
    C.append(A[i] + B[i])

ok = []

for i in range(X):
    ind = A.index(max(A))
    ok.append(ind+1)
    A[ind] = -1
    B[ind] = -1
    C[ind] = -1

for i in range(Y):
    ind = B.index(max(B))
    ok.append(ind+1)
    B[ind] = -1
    C[ind] = -1

for i in range(Z):
    ind = C.index(max(C))
    ok.append(ind+1)
    C[ind] = -1


ok.sort()

for ans in ok:
    print(ans)
