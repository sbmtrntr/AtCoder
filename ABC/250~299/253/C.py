q = int(input())

query = []

for i in range(q):
    query.append(list(map(int, input().split())))

s = {}

for i in range(q):
    if query[i][0] == 1:
        if query[i][1] not in s:
            s[query[i][1]] = 1
        else:
            s[query[i][1]] += 1

    elif query[i][0] == 2:
        if query[i][1] in s:
            s[query[i][1]] -= min(query[i][2], s[query[i][1]])
            if s[query[i][1]] == 0:
                del s[query[i][1]]
    
    else:
        dic = sorted(s)
        print(dic[-1] - dic[0])
        


