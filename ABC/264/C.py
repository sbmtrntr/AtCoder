H1, W1 = map(int, input().split())
A = []
for i in range(H1):
    A.append(list(map(int, input().split())))
H2, W2 = map(int, input().split())
B = []
for i in range(H2):
    B.append(list(map(int, input().split())))

dic_w = {}
dic_h = {}

for i in range(H1):
    for j in range(W1):
        if A[i][j] not in dic_w:
            dic_h[A[i][j]] = [i]
            dic_w[A[i][j]] = [j]
        else:
            dic_h[A[i][j]].append(i)
            dic_w[A[i][j]].append(j)

flag = True
for i in range(H2):
    w = dic_w[B[i][0]]
    for j in range(W2):
        if B[i][j] not in dic_w:
            flag = False
        else:
            if dic_w[B[i][j]][0] not in w:
                flag = False

transpose = []
for i in range(len(B[0])):
    tmp = []
    for v in B:
        tmp.append(v[i])
    transpose.append(tmp)

for i in range(W2):
    h = dic_h[transpose[i][0]]
    for j in range(H2):
        if transpose[i][j] not in dic_h:
            flag = False
        else:
            if dic_h[transpose[i][j]][0] not in h:
                flag = False

if flag:
    print("Yes")
else:
    print("No")


