N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sort_A = A.copy()
sort_A.sort()

for i in range(K):
    if sort_A[N-1] == A[B[i]-1]:
        print("Yes")
        exit()

print("No")
