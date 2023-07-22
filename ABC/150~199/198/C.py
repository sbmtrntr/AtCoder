import math

R, X, Y = map(int, input().split())

dis = math.sqrt(X**2 + Y**2)

ans = 0

while True:
    if dis == R:
        ans += 1
        break
    if dis < 2*R:
        ans += 2
        break
    else:
        ans += 1
        dis -= R
    
print(ans)
