from math import tan, pi
a, b, x = map(int, input().split())

def f(theta):
    if theta > pi / 2.0:
        return 0.0
    if a*tan(theta) <= b:
        return a * a * b - a * a * a * tan(theta) / 2.0
    else:
        return b * b / tan(theta) * a / 2.0
    
ng, ok = 0.0, pi / 2.0

while ok - ng > 0.00000001:
    mid = (ng + ok) / 2
    if f(mid) < x:
        ok = mid
    else:
        ng = mid

print(ok*(180/pi))