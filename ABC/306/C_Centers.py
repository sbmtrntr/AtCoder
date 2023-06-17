N = int(input())
A = list(map(int, input().split()))
cnt = [0]*(N+1)
ans = []
for i in range(N*3):
    cnt[A[i]] += 1
    if cnt[A[i]] == 2:
        ans.append(A[i])
print(*ans)