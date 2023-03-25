<<<<<<< HEAD
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
alpha = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = alpha[A[i][j]]

for a in ans:
=======
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
alpha = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = alpha[A[i][j]]

for a in ans:
>>>>>>> bafeeda5f8b5c60ae86c2edaeeb88702f25eca53
    print(''.join(a))