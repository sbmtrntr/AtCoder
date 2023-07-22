from itertools import product
N, T, M = map(int, input().split())
A, B = [0]*M, [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())

for per in product(range(T), repeat=N):
    print(per)