N, T = map(int,input().split())
A = list(map(int,input().split()))

accum = [0]*(N+1)
for i in range(N):
    accum[i+1] = accum[i] + A[i]

l = 0
r = N
T %= accum[-1]

while r >= l:
    mid = (l+r) // 2
    if accum[mid] > T:
        r = mid - 1
    else:
        l = mid + 1

print(l, T - accum[r])