h, w, n = map(int, input().split())

a = [0]*n
b = [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())

dic_A = {}
dic_B = {}

A = a.copy()
A = list(set(A))
A.sort()
B = b.copy()
B = list(set(B))
B.sort()

for i in range(len(A)):
    if A[i] not in dic_A:
        dic_A[A[i]] = i+1

for i in range(len(B)):
    if B[i] not in dic_B:
        dic_B[B[i]] = i+1

for i in range(n):
    print(dic_A[a[i]], dic_B[b[i]])