N = int(input())
A = list(map(int, input().split()))
mean = sum(A) // N
A.sort()
l = 0
r = N-1
ans = 0
while l < r:
    if abs(A[l] - mean) > abs(A[r] - mean):
        ans += abs(A[r] - mean)
        A[l] += abs(A[r] - mean)
        A[r] -= abs(A[r] - mean)
        r -= 1
        if abs(A[l] - mean) <= 1:
            l += 1
    else:
        ans += abs(A[l] - mean)
        A[r] -= abs(A[l] - mean)
        A[l] += abs(A[l] - mean)
        l += 1
        if abs(A[r] - mean) <= 1:
            r -= 1

for i in range(N):
    if abs(A[i] - mean) > 1:
        ans += abs(A[i] - mean) - 1

print(ans)