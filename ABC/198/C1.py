import math

R, X, Y = map(int, input().split())

Z = math.sqrt(X**2 + Y**2)

ans = 0

while True:
    if R == Z:
        ans += 1
        break
    
    if 2*R < Z:
        ans += 1
        Z -= R
    else:
        ans += 2
        break

print(ans)