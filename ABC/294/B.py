H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
alpha = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = alpha[A[i][j]]

for a in ans:
    print(''.join(a))