N = int(input())

dic = {}

for i in range(N):
    S = input()
    if S not in dic:
        print(S)
        dic[S] = 1
    else:
        print(S + '(' + str(dic[S]) + ')')
        dic[S] += 1