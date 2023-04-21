N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

for i in range(Q):
    B = int(input())
    left = 0
    right = N-1
    while right - left > 1:
        mid = (left+right)//2
        if A[mid] > B:
            right = mid
        else:
            left = mid
    
    print(min(abs(B-A[left]), abs(B-A[right])))