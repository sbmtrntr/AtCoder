h, w = map(int, input().split())

a = [list(map(int, input().split())) for i in range(h)]

b = []

for i in range(w):
    tmp = []
    for j in range(h):
        tmp.append(a[j][i])
    b.append(tmp)

for ans in b:
    print(*ans)