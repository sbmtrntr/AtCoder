N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

x_left = max(A)
x_right = min(B)

if x_left <= x_right:
    print(x_right - x_left + 1)
else:
    print(0)

