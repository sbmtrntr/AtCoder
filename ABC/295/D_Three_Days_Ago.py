from collections import defaultdict
S = input()
N = len(S)
dic = defaultdict(int)
accum = [[0]*10 for _ in range(N+1)]
dic["0000000000"] += 1
for i in range(N):
    accum[i+1][int(S[i])] += 1
    for j in range(10):
        accum[i+1][j] += accum[i][j]
        accum[i+1][j] %= 2
    moji = [str(x) for x in accum[i+1]]
    dic["".join(moji)] += 1
ans = 0
for b in range(1 << 10):
    temp = ""
    for i in range(10):
        if b >> i & 1:
            temp += "1"
        else:
            temp+= "0"
    if temp in dic:
        ans += dic[temp]*(dic[temp]-1)//2
print(ans)