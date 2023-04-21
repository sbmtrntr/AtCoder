N =int(input())

A = list(map(int, input().split()))

dic = {}

for i in range(N*4-1):
    if A[i] not in dic:
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1

for k, v in dic.items():
    if v == 3:
        print(k)