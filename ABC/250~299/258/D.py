N, X = map(int, input().split())

A, B, C = [], [], [0]

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(a+b+C[-1])

ans = 10**30

for i in range(N):
    if i+1 <= X:
        ans = min(C[i+1] + B[i]*(X-i-1), ans)

print(ans)

