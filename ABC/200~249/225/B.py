N = int(input())

AB = [tuple(map(int, input().split())) for _ in range(N-1)]

dic = {}
for a, b in AB:
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1
    if b not in dic:
        dic[b] = 1
    else:
        dic[b] += 1
    
for v in dic.values():
    if v == N-1:
        print('Yes')
        exit()

print('No')