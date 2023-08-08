N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

X = []
Y = set()

for i in range(N):
    for j in range(N):
        X.append(A[i] + B[j])
        Y.add(C[i] + D[j])

for x in X:
    if K - x in Y:
        print('Yes')
        exit()

print('No')