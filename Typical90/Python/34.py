from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)

l = -1
r = -1
ans = 0

while l < N:
    if len(cnt) <= K and r < N:
        ans = max(ans, r-l)
        r += 1
        if r < N:
            cnt[A[r]] += 1
    else:
        l += 1
        if l < N:
            cnt[A[l]] -= 1
            if cnt[A[l]] == 0:
                cnt.pop(A[l])

print(ans)