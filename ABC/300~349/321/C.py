from itertools import product
K = int(input())
ans = []
num = "9876543210"
for pro in product([0, 1], repeat=10):
    temp = ""
    for i in range(10):
        if pro[i] == 0:
            temp += str(num[i])
    if temp != '':
        ans.append(int(temp))

ans.sort()
print(ans[K])