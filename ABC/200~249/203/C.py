N, K = map(int, input().split())

AB = []
for i in range(N):
    AB.append(list(map(int, input().split())))

AB.sort()

for i in range(N):
    if K < AB[i][0]:
        break

    K += AB[i][1]

print(K)