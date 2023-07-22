N, M = map(int, input().split())

tree = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    tree[u][v] = tree[v][u] = 1

ans = 0
for i in range(N):
    for j in range(N):
        if tree[i][j] == 1:
            for k in range(N):
                if tree[j][k] == 1 and k != i and tree[k][i] == 1:
                    ans += 1
                

print(ans//6)

