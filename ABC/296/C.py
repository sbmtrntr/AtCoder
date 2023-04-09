N, X = map(int, input().split())
A = list(map(int, input().split()))

setA = set(A)

for i in range(N):
    if A[i] - X in setA:
        exit(print('Yes'))

print('No')