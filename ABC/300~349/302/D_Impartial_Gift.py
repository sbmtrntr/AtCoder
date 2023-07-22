from bisect import bisect
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = -1

A.sort()
B.sort()

for i in range(N):
    idx = bisect(B, A[i]+D)
    if idx == 0:
        if abs(A[i] - B[idx]) <= D:
            ans = max(ans, A[i] + B[idx])
    elif idx == M:
        if abs(A[i] - B[idx-1]) <= D:
            ans = max(ans, A[i] + B[idx-1])
    else:
        if abs(A[i] - B[idx]) <= D:
            ans = max(ans, A[i] + B[idx])
        if abs(A[i] - B[idx-1]) <= D:
            ans = max(ans, A[i] + B[idx-1])

print(ans)