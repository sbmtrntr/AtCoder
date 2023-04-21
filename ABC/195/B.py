import math

A, B, W = map(int, input().split())
W *= 1000

upper = int(math.floor(W / A))
lower = int(math.ceil(W / B))

if lower > upper:
    print("UNSATISFIABLE")
else:
    print(lower, upper)