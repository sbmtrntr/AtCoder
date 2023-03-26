A = []
B = 0
while right - left > 1:
    mid = (left+right)//2
    if A[mid] > B:
        right = mid
    else:
        left = mid