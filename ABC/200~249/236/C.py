N, M = map(int, input().split())

S = list(input().split())
T = list(input().split())

dic = {}

for i in range(M):
    dic[T[i]] = True

for s in S:
    try:
        if dic[s]:
            print('Yes')
    except:
        print('No')