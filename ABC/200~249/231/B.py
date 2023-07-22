N = int(input())

dic = {}

for i in range(N):
    s = input()
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

print((max(dic, key = dic.get)))