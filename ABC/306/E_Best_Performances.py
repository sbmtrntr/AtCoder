from bisect import bisect
N, K, Q = map(int, input().split())
A = [0]*N
B = [0]*K
for _ in range(Q):
    x, y = map(int, input().split())
    l = 0
    r = K
    while l > r:
        mid = (l+r)//2
        if B[mid] == A[x-1]:
            break
        elif B[mid] > A[x-1]:
            r = mid
        else:
            l = mid
    