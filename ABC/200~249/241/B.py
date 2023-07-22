N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    for j in range(len(A)):
        if B[i] == A[j]:
            del A[j]
            break
        if j == len(A)-1:
            print('No')
            exit()


print('Yes')