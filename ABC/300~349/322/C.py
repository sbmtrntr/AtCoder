from bisect import bisect_left
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    idx = bisect_left(A, i+1)
    print(A[idx] - (i+1))