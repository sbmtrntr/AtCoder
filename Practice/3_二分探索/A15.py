N = int(input())
A = list(map(int, input().split()))
B = list(set(A))
B.sort()

for i in range(N):
    left = 0
    right = len(B)-1
    while left <= right:
        mid = (left + right) // 2
        if B[mid] < A[i]:
            left = mid + 1
        else:
            right = mid - 1
    A[i] = left + 1
print(*A)