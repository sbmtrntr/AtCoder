N, A, B = map(int, input().split())

ans = 0
for i in range(1, N+1):
    sm = 0
    for j in str(i):
        sm += int(j)
    if A <= sm <= B:
        ans += i

print(ans)
