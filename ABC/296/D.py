N, M = map(int, input().split())
ans = 10**13

for i in range(1, N+1):
    x = (M+i-1)//i
    if x <= N:
        ans = min(ans, i*x)
    if i > x:
        break
    
if ans == 10**13:
    print(-1)
else:
    print(ans)