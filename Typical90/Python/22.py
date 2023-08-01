import math

A, B, C = map(int, input().split())

length = math.gcd(A, B)
length = math.gcd(length, C)

print(A//length + B//length + C//length -3)