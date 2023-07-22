N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(1, N, 2):
    A[i] -= 1

if sum(A) <= X: print("Yes")
else: print('No')
