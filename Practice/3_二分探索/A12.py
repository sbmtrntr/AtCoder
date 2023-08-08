N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 10**9

while left <= right:
    mid = (left + right) // 2
    num = 0
    for i in range(N):
        num += mid // A[i]
    
    if num < K:
        left = mid + 1
    else:
        right = mid - 1

print(left)