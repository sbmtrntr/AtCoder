N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N-1

while left <= right:
    middle = (left + right) // 2
    if A[middle] > X:
        right = middle - 1
    elif A[middle] == X:
        print(middle+1)
        break
    else:
        left = middle + 1