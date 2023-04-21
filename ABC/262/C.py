N = int(input())
A = list(map(int, input().split()))

x = 0
ans = 0

for i in range(N):
    if i + 1 == A[i]:
        x += 1
    else:
        if A[A[i]-1] == i+1:
            ans += 1

ans //= 2


if x != 1 or x != 0:
    ans += x*(x-1)//2

print(ans)
