N, M = map(int, input().split())
Ss = [input() for _ in range(N)]

ans = 0
for i in range(N-1):
    temp = [0]*M
    for j in range(M):
        if Ss[i][j] == "o":
            temp[j] = 1
    for j in range(i+1, N):
        temp1 = temp.copy()
        for k in range(M):
            if Ss[j][k] == "o":
                temp1[k] = 1

        if sum(temp1) == M:
            ans += 1

print(ans)
