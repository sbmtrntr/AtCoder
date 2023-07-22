Ha, Wa = map(int, input().split())
A = [input() for _ in range(Ha)]
Hb, Wb = map(int, input().split())
B = [input() for _ in range(Hb)]
Hx, Wx = map(int, input().split())
X = [input() for _ in range(Hx)]

C = ['.'*10 for _ in range(10)]


for x in range(10):
    for y in range(10):
        C = [['.']*10 for _ in range(10)]
        for i in range(Ha):
            for j in range(Wa):
                if A[i][j] == '#' and x+i < 10 and y+j < 10:
                    C[x+i][y+j] = '#'
        for i in range(Hb):
            for j in range(Wb):
                if B[i][j] == '#' and x+i < 10 and y+j < 10:
                    C[x+i][y+j] = '#'
        flag = True
        for i in range(Hx):
            for j in range(Wx):
                if X[i][j] != C[x+i][y+j]:
                    flag = False
        if flag:
            print('Yes')
            exit()
print('No')