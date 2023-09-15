from bisect import bisect_right, bisect_left
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

def f(x):
    return bisect_right(A, x)

def g(x):
    return M - bisect_left(B, x)

left = 0
right = 10**9

while right - left > 1:
    mid = (right + left) // 2
    if f(mid) >= g(mid):
        right = mid
    else:
        left = mid

print(right)