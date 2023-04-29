H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [0]*(min(H, W))

def check(a, b, n):
    hoge = 0
    for d in range(1, n+1):
        if a+d < H and b+d < W and 0 <= b-d and 0 <= a-d:
            if C[a+d][b+d] == '#' and C[a+d][b-d] == '#' and C[a-d][b+d] == '#' and C[a-d][b-d] == '#':
                hoge = d
            else:
                return hoge
        
    return hoge



for i in range(1, H-1):
    for j in range(1, W-1):
        if C[i][j] == '#':
            num = check(i, j, 50)
            if num == 0:
                pass
            else:
                ans[num-1] += 1

print(*ans)