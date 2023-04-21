H, W = map(int, input().split())

A = []

for i in range(H):
    A.append(list(map(int, input().split())))
A_T = list(zip(*A))

B = [[0 for _ in range(W)] for _ in range(H)]

Row = [0 for _ in range(H)]
Column = [0 for _ in range(W)]

for i in range(H):
    Row[i] = sum(A[i])

for i in range(W):
    Column[i] = sum(A_T[i])

for i in range(H):
    for j in range(W):
        B[i][j] += Row[i] + Column[j] - A[i][j]
        
for b in B:
    print(*b)