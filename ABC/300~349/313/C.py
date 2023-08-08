N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
p = sum(A) // N
r = sum(A) % N

for i in range(N-r):
    ans += abs(A[i] - p)
for i in range(N-r, N):
    ans += abs(A[i] - (p + 1))

print(ans//2)