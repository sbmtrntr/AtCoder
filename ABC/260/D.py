N, K =map(int, input().split())
P = list(map(int, input().split()))

ans = [-1]*N
dic = {}
dic[0] = [P[0], [P[0]]]
m = 1

if K == 1:
    for i in range(N):
        ans[P[i]-1] = i + 1
    for a in ans:
        print(a)
    exit()

for i in range(1, N):
    flag = True
    for k, v in dic.items():
        if P[i] <= v[0]:
            v[0] = P[i]
            v[1].append(P[i])
            flag = False
            if len(v[1]) == K:
                for vv in v[1]:
                    ans[vv-1] = i+1
                del dic[k]
            break
    
    if flag:
        dic[m] = [P[i], [P[i]]]
        m += 1

for a in ans:
    print(a)