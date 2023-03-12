N, Q = map(int, input().split())
a = [0]*N
for i in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        a[x-1] += 1
    elif n == 2:
        a[x-1] += 2
    else:
        if a[x-1] >= 2:
            print('Yes')
        else:
            print('No')
