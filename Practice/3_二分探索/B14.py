from itertools import product
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []

for i in range(N//2):
    B.append(A.pop())

C = []
for pro in product((0, 1), repeat=len(A)):
    temp = 0
    for i in range(len(A)):
        if pro[i]:
            temp += A[i]
    C.append(temp)

D = set()
for pro in product((0, 1), repeat=len(B)):
    temp = 0
    for i in range(len(B)):
        if pro[i]:
            temp += B[i]
    D.add(temp)

for c in C:
    if K - c in D:
        exit(print('Yes'))

print('No')