N = int(input())

L, R, = [], []
for i in range(N):
    t, l, r, = map(int, input().split())
    if t == 1:
        L.append(l)
        R.append(r)
    elif t == 2:
        L.append(l)
        R.append(r-0.5)
    elif t == 3:
        L.append(l+0.5)
        R.append(r)
    else:
        L.append(l+0.5)
        R.append(r-0.5)

ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        if max(L[i], L[j]) <= min(R[i], R[j]):
            ans += 1

print(ans)


