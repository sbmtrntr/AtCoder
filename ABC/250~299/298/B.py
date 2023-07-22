N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        exit(print('Yes'))
    else:
        temp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                temp[i][j] = A[N-j-1][i]
        A = temp
print('No')