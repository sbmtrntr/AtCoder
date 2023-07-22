N, W = map(int, input().split())

A = list(map(int, input().split()))

ans = [False]*(W+1)

for i in range(N):
    if A[i] <= W:
        ans[A[i]] = True

for i in range(N-1):
    for j in range(i+1, N):
        if A[i] + A[j] <= W:
            ans[A[i] + A[j]] = True

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] <= W:
                ans[A[i] + A[j] + A[k]] = True

print(sum(ans))


