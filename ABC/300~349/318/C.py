N, D, P = map(int,input().split())
F = list(map(int,input().split()))
F.sort(reverse=True)
idx = 0
ans = 0
while idx != N:
    cnt = 0
    for i in range(D):
        cnt += F[idx]
        idx += 1
        if idx == N:
            break
    if cnt > P:
        ans += P
    else:
        if idx != N:
            ans += sum(F[idx-D:])
            break
        else:
            ans += sum(F[idx-(i+1):])

print(ans)