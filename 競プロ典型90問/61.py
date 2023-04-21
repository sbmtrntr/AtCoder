Q = int(input())

tehuda1 = []
tehuda2 = []

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        tehuda1.append(x)
    elif t == 2:
        tehuda2.append(x)
    else:
        if x <= len(tehuda1):
            print(tehuda1[len(tehuda1)-x])
        else:
            print(tehuda2[x-len(tehuda1)-1])

        