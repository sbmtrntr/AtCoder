N, M = map(int, input().split())

B = []

for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if B[i][j] % 7 == 0 and j != M-1:
            print('No')
            exit()
            
C = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if j == 0:
            C[i][0] = B[0][0] + 7*i
        else:
            C[i][j] = C[i][j-1] + 1

if B == C:
    print('Yes')
else:
    print('No')