N, Q = map(int, input().split())
A = list(map(int, input().split()))

ind = 0
for i in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        A[(x-ind)%N], A[(y-ind)%N] = A[(y-ind)%N], A[(x-ind)%N]
    elif t == 2:
        ind += 1
    else:
        print(A[(x-ind)%N])
