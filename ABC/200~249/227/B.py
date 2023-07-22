N = int(input())
S = list(map(int, input().split()))

#面積としてあり得るやつを全探索
T = []
for a in range(1, 143):
    for b in range(1, 143):
        t = 4*a*b + 3*a + 3*b
        if t <= 1000:
            T.append(t)
        else:
            break

ans = 0

#予想されたものがTの中になかったらカウント
for i in range(N):
    if S[i] not in T: 
        ans += 1

print(ans)