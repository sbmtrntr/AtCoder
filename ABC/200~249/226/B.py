N = int(input())

L, a = [], []

for i in range(N):
    temp = list(map(int, input().split()))
    L.append(temp[0])
    a.append(temp[1:])

a = list(map(list, set(map(tuple, a))))

print(len(a))