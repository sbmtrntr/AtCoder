N, K = map(int, input().split())

S = [input() for _ in range(N)]

ans = 0

for b in range(1 << N):
    temp = []
    for i in range(N):
        if b >> i & 1:
            temp.append(S[i])
    
    dic = {}
    for x in temp:
        for j in range(len(x)):
            if x[j] not in dic:
                dic[x[j]] = 1
            else:
                dic[x[j]] += 1
    
    temp_ans = 0
    for v in dic.values():
        if v == K:
            temp_ans += 1
    
    ans = max(ans, temp_ans)

print(ans)
