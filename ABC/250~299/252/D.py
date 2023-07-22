N = int(input())

A = list(map(int, input().split()))

X = {}

for i in range(N):
    if A[i] not in X:
        X[A[i]] = 1
    else:
        X[A[i]] += 1

import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = comb(N,3)

for v in X.values():
    if v != 1:
        ans -= v

print(ans)