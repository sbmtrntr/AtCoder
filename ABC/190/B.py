N, S, D = map(int, input().split())

X, Y = [0]*N, [0]*N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

for i in range(N):
    if X[i] >= S or Y[i] <= D:
        continue
    else:
        print('Yes')
        exit()

print('No')