N, M = map(int, input().split())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i+8 < N and j+8 < M:
            flag = True
            for x in range(3):
                for y in range(3):
                    if S[i+x][j+y] != '#':
                        flag = False
                    if S[i+x+6][j+y+6] != '#':
                        flag = False
            if S[i][j+3] != '.' or S[i+1][j+3] != '.' or S[i+2][j+3] != '.' or S[i+3][j+3] != '.' or S[i+3][j+2] != '.' or S[i+3][j+1] != '.' or S[i+3][j] != '.':
                flag = False
            if S[i+5][j+8] != '.' or S[i+5][j+7] != '.' or S[i+5][j+6] != '.' or S[i+5][j+5] != '.' or S[i+6][j+5] != '.' or S[i+7][j+5] != '.' or S[i+8][j+5] != '.':
                flag = False
            if flag:
                print(i+1, j+1)