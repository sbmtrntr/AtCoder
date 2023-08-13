N = int(input())

left = 0.0
right = 100.0

while left <= right:
    mid = (left + right) / 2
    if mid**3 + mid < N:
        left = mid + 0.001
    else:
        right = mid - 0.001

print(right)