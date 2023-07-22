h, w = map(int,input().split())
ans = 0
for _ in range(h):
    s = input()
    for i in range(w):
        if s[i] == '#':
            ans += 1
print(ans)