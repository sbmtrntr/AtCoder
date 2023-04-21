N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    for j in range(i+1, N):
        A[i] += A[j]

ans = 0

for i in A:
    if i >= 4:
        ans += 1

print(ans)

