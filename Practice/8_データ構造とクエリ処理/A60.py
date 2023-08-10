Q = int(input())
s = set()

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        s.add(q[1])
    elif q[0] == 2:
        s.remove(q[1])
    else:
        temp = []
        for x in s:
            temp.append(x)