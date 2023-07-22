N, A, X, Y = map(int, input().split())

ans = 0

for i in range(N):
    if i > A-1:
        ans += Y
    else:
        ans += X
    
print(ans)