from bisect import bisect_left
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

for i in range(N):
    idx = bisect_left(B, A[i])
    if idx == M:
        continue
    if i+1 >= M - idx:
        print(A[i])
        exit()
print(B[-1]+1)