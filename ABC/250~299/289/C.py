N, M = map(int, input().split())
S = []
for i in range(M):
    c = int(input())
    S.append(list(map(int, input().split())))
ans = 0
for b in range(1 << M):
    temp = set()
    for i in range(M):
        if b >> i & 1:
            for j in range(len(S[i])):
                temp.add(S[i][j])

    flag = True
    for x in range(1, N+1):
        if x not in temp:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
