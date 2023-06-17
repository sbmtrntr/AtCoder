import bisect
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
accum = [0]
for i in range(1, N, 2):
    hoge = A[i+1] - A[i]
    accum.append(accum[-1] + hoge)

for _ in range(Q):
    l, r = map(int, input().split())
    l_idx = bisect.bisect(A, l)
    r_idx = bisect.bisect(A, r)
    minus = 0
    if l_idx % 2 == 0:
        minus = l - A[l_idx-1]
    if r_idx % 2 == 0:
        minus += A[r_idx] - r
    print(accum[r_idx//2] - accum[(l_idx-1)//2] - minus)