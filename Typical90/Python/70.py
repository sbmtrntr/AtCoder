import numpy as np
N = int(input())
X, Y = [0]*N, [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

median_x, median_y = np.median(X), np.median(Y)

ans = 0
for i in range(N):
    ans += abs(X[i] - median_x) + abs(Y[i] - median_y)

print(int(ans))