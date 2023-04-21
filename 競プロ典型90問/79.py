H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

C = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        C[i][j] = A[i][j] -B[i][j]

cnt = 0

for i in range(H-1):
    for j in range(W-1):
        if C[i][j] == 0:
            continue
        else:
            C[i+1][j] -= C[i][j]
            C[i][j+1] -= C[i][j]
            C[i+1][j+1] -= C[i][j]
            cnt += abs(C[i][j])
            C[i][j] = 0

zero_masu = [[0 for _ in range(W)] for _ in range(H)]

if C == zero_masu:
    print('Yes')
    print(cnt)
else:
    print('No')


