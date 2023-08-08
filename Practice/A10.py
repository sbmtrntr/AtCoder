from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
D = int(input())

memo = defaultdict(int)
mx = -1
idx = -1
for i in range(N):
    if mx <= A[i]:
        mx = A[i]
        idx = i
        memo[i+1] = idx
    else:
        memo[i+1] = idx

memo1 = defaultdict(int)
mx = -1
idx = -1
for i in range(N-1, -1, -1):
    if mx <= A[i]:
        mx = A[i]
        idx = i
        memo1[i+1] = idx
    else:
        memo1[i+1] = idx

for i in range(D):
    L, R = map(int, input().split())
    print(max(A[memo[L-1]], A[memo1[R+1]]))