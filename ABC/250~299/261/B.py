N = int(input())
A = []
for i in range(N):
    A.append(list(input()))

flag = True
for i in range(N):
    for j in range(N):
        if A[i][j] == '-' and A[j][i] != '-':
            flag = False
        elif A[i][j] == 'W' and A[j][i] != 'L':
            flag = False
        elif A[i][j] == 'L' and A[j][i] != 'W':
            flag = False
        elif A[i][j] == 'D' and A[j][i] != 'D':
            flag = False


if flag:
    print('correct')
else:
    print('incorrect')
