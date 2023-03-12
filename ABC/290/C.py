N, K = map(int, input().split())
A = list(set((map(int, input().split()))))
A.sort()
now = -1
if len(A) < K:
    for i in range(len(A)):
        if A[i] == now+1:
            now += 1
        else:
            exit(print(now+1))
else:
    for i in range(K):
        if A[i] == now+1:
            now += 1
        else:
            exit(print(now+1))


print(now+1)