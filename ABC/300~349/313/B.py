N, M = map(int, input().split())
A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

saikyo = set()
not_saikyo = set()
for i in range(M):
    if A[i] not in not_saikyo:
        saikyo.add(A[i])
    if B[i] in saikyo:
        saikyo.remove(B[i])
    not_saikyo.add(B[i])

if len(saikyo) == 1:
    print(*saikyo)
else:
    print(-1)