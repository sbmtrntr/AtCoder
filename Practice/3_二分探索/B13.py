N, K = map(int, input().split())
A = list(map(int, input().split()))
accum = [0]*(N+1)
ans = 0
for i in range(N):
    accum[i+1] += accum[i] + A[i]

for i in range(N):
    if A[i] <= K:
        ans += 1

l = 1
while l != N:
    r = l+1
    while r != N+1:
        if accum[r] - accum[l-1] <= K:
            ans += 1
        else:
            break
        r += 1
    l += 1

print(ans)