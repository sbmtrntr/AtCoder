N = int(input())
S = input()

coord = set()
now = [0, 0]
coord.add((0, 0))

for i in range(N):
    if S[i] == 'R':
        now[0] += 1
    elif S[i] == 'L':
        now[0] -= 1
    elif S[i] == 'U':
        now[1] += 1
    else:
        now[1] -= 1
    hoge = tuple(now)
    if hoge in coord:
        exit(print('Yes'))
    coord.add(hoge)

print('No')