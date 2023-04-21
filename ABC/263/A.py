X = list(map(int, input().split()))

dic = {}

for i in range(5):
    if X[i] not in dic:
        dic[X[i]] = 1
    else:
        dic[X[i]] += 1

flag = 0
flag1 = 0
for v in dic.values():
    if v == 3:
        flag = 1
    elif v == 2:
        flag1 = 1

if flag1 and flag:
    print("Yes")
else:
    print("No")

