N, Q = map(int, input().split())

a = list(range(N+1))
inv = list(range(N+1))

for _ in range(Q):
    x = int(input())
    pos_x = inv[x]
    if pos_x == N:
        pos_y = pos_x - 1
    else:
        pos_y = pos_x + 1
    y = a[pos_y]

    a[pos_x], a[pos_y] = a[pos_y], a[pos_x]
    inv[x], inv[y] = inv[y], inv[x]

print(*a[1:])
    
