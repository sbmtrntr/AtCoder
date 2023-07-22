N, K = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

AB.sort()
nomu = 0
for i in range(N):
    nomu += AB[i][1]

if nomu <= K:
    print(1)
    exit()
for i in range(N):
    nomu -= AB[i][1]
    if nomu <= K:
        print(AB[i][0]+1)
        break