N = int(input())
A = list(map(int, input().split()))
ans = [0]*N
for i in range(N*7):
    ans[i//7] += A[i]
print(*ans)