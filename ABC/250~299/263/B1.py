N = int(input())
P = list(map(int, input().split()))

for i in range(N-1):
    P[i] -= 1

ans = 1
ind = P[-1]

for i in range(N-1):
    if ind == 0:
        print(ans)
        break
    else:
        ind = P[ind-1]
        ans += 1
