N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        temp = S[i] + S[j]
        flag = True
        for k in range(len(temp)):
            if temp[k] != temp[len(temp)-k-1]:
                flag = False
                break

        if flag:
            exit(print('Yes'))
print('No')