S = input()
N = int(input())
min_T = S.replace('?', '0')
if int(min_T, 2) > N:
    print(-1)
else:
    min_T = list(min_T)
    for i in range(len(S)):
        if S[i] == '?':
            min_T[i] = '1'
        if int("".join(min_T), 2) > N:
            min_T[i] = '0'
    print(int("".join(min_T), 2))