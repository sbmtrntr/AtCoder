from itertools import product
H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]
ans = 0

def paint_row(d, remain):
    columns = []
    for j in range(W):
        temp = 0
        for i in range(H):
            if d[i][j] == ".":
                temp += 1
        columns.append((temp, j))
    columns.sort(reverse=True)

    for j in range(remain):
        idx = columns[j][1]
        for i in range(H):
            d[i][idx] = '#'

    temp = 0
    for i in range(H):
        for j in range(W):
            if d[i][j] == "#": temp += 1
    
    return temp


for v in product([0, 1], repeat=H):
    d = [ list(c[i]) for i in range(H) ]
    remain = K
    for i in range(H):
        if v[i] == 1:
            d[i] = ['#']*W
            remain -= 1
    if remain >= 0:
        temp = paint_row(d, remain)
        ans = max(ans, temp)

print(ans)