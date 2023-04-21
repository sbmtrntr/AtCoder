N, K = map(int, input().split())

points = [0]*(2*N)

for i in range(N):
    a, b = map(int, input().split())
    a -= b
    points[2*i] = b
    points[2*i+1] = a

points.sort(reverse=True)

ans = 0
for i in range(K):
    ans += points[i]

print(ans)
