N, K = map(int, input().split())

c = list(map(int, input().split()))

color = {}
ans = 0

for i in range(K):
    if c[i] not in color:
        color[c[i]] = 1
    else:
        color[c[i]] += 1

ans = max(ans, len(color))

for i in range(K, N):
    color[c[i-K]] -= 1
    if color[c[i-K]] == 0:
        del color[c[i-K]]

    if c[i] not in color:
        color[c[i]] = 1
    else:
        color[c[i]] += 1
        
    ans = max(ans, len(color))

print(ans)
