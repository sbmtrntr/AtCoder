N, M, H, K = map(int, input().split())
S = input()
items = set()
for _ in range(M):
    x, y = map(int, input().split())
    items.add((x, y))

coord = [0, 0]

for i in range(N):
    H -= 1

    if S[i] == 'R':
        coord[0] += 1
    elif S[i] == 'L':
        coord[0] -= 1
    elif S[i] == 'U':
        coord[1] += 1
    else:
        coord[1] -= 1

    if H < 0:
        exit(print('No'))
    else:
        if (coord[0], coord[1]) in items and H < K:
            H = K
            items.remove((coord[0], coord[1]))
print('Yes')