N, M = map(int, input().split())
L = list(map(int, input().split()))

def can_fit(W):
    line_width = 0
    lines = 1
    
    for i in range(N):
        if line_width + L[i] <= W:
            line_width += L[i] + 1
        else:
            lines += 1
            line_width = L[i] + 1
    
    return lines <= M


left, right = max(L), 10**15

while left < right:
    mid = (left + right) // 2
    if can_fit(mid):
        right = mid
    else:
        left = mid + 1

print(left)