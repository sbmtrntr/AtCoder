N = int(input())
S = [3] * N
S[0] = 0
S[-1] = 1
left = 0
right = N-1
mid = (left + right) // 2
while right - left > 1:
    print('?', str(mid+1))
    num = int(input())
    S[mid] = num
    if abs(S[mid] - S[mid+1]) == 1:
        print('!', str(mid+1))
        exit()
    if abs(S[mid-1] - S[mid]) == 1:
        print('!', str(mid))
        exit()
    if num == 1:
        right = mid
    else:
        left = mid
    mid = (left + right) // 2

if abs(S[mid] - S[mid+1]) == 1:
    print('!', str(mid+1))
    exit()
if abs(S[mid-1] - S[mid]) == 1:
    print('!', str(mid))
    exit()