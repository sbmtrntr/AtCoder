N, M = map(int, input().split())
A = [""]

for i in range(2*N):
    A.append(input())

win_cnt = {}

for i in range(2*N):
    win_cnt[i+1] = 0

juni = {}

for i in range(2*N):
    juni[i+1] = i+1

def win(te1, te2):
    if te1 == "G" and te2 == "C":
        return 1
    elif te1 == "C" and te2 == "P":
        return 1
    elif te1 == "P" and te2 == "G":
        return 1
    elif te1 == "C" and te2 == "C":
        return 2
    elif te1 == "G" and te2 == "G":
        return 2
    elif te1 == "P" and te2 == "P":
        return 2
    else:
        return 3

for i in range(1, M+1): #iラウンド
    for j in range(1, N+1): #j番目の試合
        for k, v in juni.items():
            if v == 2*j-1: 
                te1 = A[k][i-1]
                x = k
            elif v == 2*j:
                te2 = A[k][i-1]
                y = k

        if win(te1, te2) == 1:
            win_cnt[x] += 1
        elif win(te1, te2) == 2:
            continue
        else:
            win_cnt[y] += 1

    n = 1
    for z in range(i, -1, -1):
        for k, v in win_cnt.items():
            if v == z:
                juni[k] = n
                n += 1

for i in range(1, 2*N+1):
    for k, v in juni.items():
        if i == v:
            print(k)
            break



