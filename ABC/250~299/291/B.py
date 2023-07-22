N = int(input())
X = list(map(int, input().split()))

X.sort()
ans = 0
for i in range(N, 4*N):
    ans += X[i]

print(ans / (3*N))