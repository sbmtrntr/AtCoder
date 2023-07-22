H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for b in range((1 << H+W-2)):
    temp = ""
    seen = set()
    seen.add(A[0][0])
    for i in range(H+W-2):
        if b >> i & 1:
            temp += "1"
        else:
            temp += "0"
    cnt = 0
    for s in temp:
        if s == "0":
            cnt += 1

    if cnt == H-1:
        x, y = 0, 0
        for s in temp:
            if s == "0":
                x += 1
            else:
                y += 1    
            seen.add(A[x][y])
        if len(seen) == H+W-1:
            ans += 1

print(ans)