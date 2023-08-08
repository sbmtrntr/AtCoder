N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(N-1):
    left = i
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] <= A[i] + K:
            left = mid + 1
        else:
            right = mid - 1
    ans += right - i

print(ans)