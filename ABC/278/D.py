N = int(input())
A = list(map(int, input().split()))
Q = int(input())
x = 0
y = []
sabun = [0]*N
reset = False
for _ in range(Q):
    qu = list(map(int, input().split()))

    if qu[0] == 1:
        x = qu[1]
        for i in range(len(y)):
            sabun[y[i]] = 0
        y = []
        reset = True
    elif qu[0] == 2:
        if reset:
            sabun[qu[1]-1] += qu[2]
        else:
            A[qu[1]-1] += qu[2]
        y.append(qu[1]-1)
    else:
        if reset:
            print(sabun[qu[1]-1] + x)
        else:
            print(A[qu[1]-1] + x)