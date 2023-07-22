import math 

A, B = map(int, input().split())

x = A/math.sqrt(A**2 + B**2)
y = B/math.sqrt(A**2 + B**2)

print(x, y)