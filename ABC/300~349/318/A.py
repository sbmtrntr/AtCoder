N, M, P = map(int,input().split())
ans = 0
x = 0
for i in range(1, N+1):
    if i == M + P*x:
        ans += 1
        x += 1

print(ans)