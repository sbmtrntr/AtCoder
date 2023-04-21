N, K = map(int, input().split())

a = list(map(int, input().split()))

cnt = K//N
Q = K % N

x = []

for i in range(N):
    x.append([a[i], i])

x.sort()

ans = [0]*N

for i in range(N):
    if i < Q:
        ans[x[i][1]] = cnt+1
    else:
        ans[x[i][1]] = cnt

for e in ans:
    print(e)

