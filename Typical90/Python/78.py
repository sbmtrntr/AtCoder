N, M = map(int, input().split())

tree = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a < b:
        tree[b] += 1    
    else:
        tree[a] += 1

ans = 0

for x in tree:
    if x == 1:
        ans += 1

print(ans)