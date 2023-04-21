N = int(input())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

sum_ab = 0
for i in range(N):
    sum_ab += A[i]/B[i]

t = 0.5*sum_ab

left = 0

for i in range(N):
    left += min(A[i], t*B[i])
    t -= min(A[i]/B[i], t)

print(left)

