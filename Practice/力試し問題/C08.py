N = int(input())
ans = [False]*N

for _ in range(N):
    s, t = map(int, input().split())
    if t == 1:
        exit(print(s))
    elif t == 2:
        for i in range(4):

    else:
        for i in range(4):
            for a in ans:
                if a[i] == t[i]:
                    ans.remove(a)