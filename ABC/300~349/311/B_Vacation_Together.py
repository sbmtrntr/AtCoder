N, D = map(int, input().split())
S = [input() for _ in range(N)]
ans = [0]*(D+1)
for i in range(D):
    flag = True
    for j in range(N):
        if S[j][i] == 'x':
            flag = False
            break
    if flag:
        ans[i+1] = ans[i] + 1

print(max(ans))