from collections import defaultdict
N, Q = map(int, input().split())

dic = defaultdict(set)

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        dic[b].add(a)
    elif t == 2:
        try:
            dic[b].remove(a)
        except:
            continue
    else:
        if b in dic[a] and a in dic[b]:
            print("Yes")
        else:
            print("No")
    

