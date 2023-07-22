N, M = map(int, input().split())
P, C, F = [], [], []
for i in range(N):
    hoge = list(map(int, input().split()))
    P.append(hoge[0])
    C.append(hoge[1])
    F.append(set(hoge[2:]))

for i in range(N):
    for j in range(N):
        flag = True
        if P[i] >= P[j]:
            for x in F[i]:
                if x not in F[j]:
                    flag = False
                    break
            if flag:
                if P[i] > P[j]:
                    exit(print('Yes'))
                for x in F[j]:
                    if x not in F[i]:
                        exit(print('Yes'))
            
print('No')