N = int(input())
P = list(map(int, input().split()))

if N == 2:
    print(1)
    exit()

tree = [[False for _ in range(N)]for _ in range(N)]

tree[0][1] = tree[1][0] = True

for i in range(N-1):
    tree[i+1][P[i]-1] = tree[P[i]-1][i+1] = True

ans = 1

for i in range(N):
    if tree[N-1][i]:
        ind = i

for i in range(N):
    ans += 1
    for j in range(N):
        if tree[ind][j]:
            ind = j
            if j == 0:
                print(ans)
                exit()
            else:
                break
    