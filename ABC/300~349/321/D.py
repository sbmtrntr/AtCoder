from bisect import bisect_right
N, M, P = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

accum_A = [0]*(N+1)
accum_B = [0]*(M+1)

for i in range(N):
    accum_A[i+1] = accum_A[i] + A[i]

for i in range(M):
    accum_B[i+1] = accum_B[i] + B[i]

ans = 0

for i in range(N):
    idx = bisect_right(B, P-A[i])
    ans += (accum_B[idx] + A[i]*idx) + P*(M-idx)

print(ans)