N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

for i in range(N):
    K -= A[i]//X
    A[i] -= (A[i]//X)*X
    if K == 0:
        break
    
    if K < 0:
        A[i] += X*(-K)
        K = 0
        

A.sort(reverse=True)

i = 0

while K > 0:
    if i == N:
        break
    A[i] = 0
    i += 1
    K -= 1


print(sum(A))


