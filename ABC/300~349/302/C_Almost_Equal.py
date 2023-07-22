from itertools import permutations
N, M = map(int, input().split())
S = [input() for _ in range(N)]

for iter in permutations(range(N), N):
    temp = []
    for i in iter:
        temp.append(S[i])
    flag = True
    for i in range(N-1):
        dif = 0
        for j in range(M):
            if temp[i][j] != temp[i+1][j]:
                dif += 1
        if dif != 1:
            flag = False
            break
    if flag:
        exit(print("Yes"))
print("No")