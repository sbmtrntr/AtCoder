N = int(input())
ans = 0
dic = {}
import math
for AB in range(1, N//2+1):
    CD = N - AB
    if AB not in dic:
        cnt = 0
        for i in range(1, int(math.sqrt(AB))+1):
            if AB % i == 0:
                j = AB // i
            else:
                continue
            if i == j:
                cnt += 1
            else:
                cnt += 2
        dic[AB] = cnt
    if CD not in dic:
        cnt = 0
        for i in range(1, int(math.sqrt(CD))+1):
            if CD % i == 0:
                j = CD // i
            else:
                continue
            if i == j:
                cnt += 1
            else:
                cnt += 2
        dic[CD] = cnt

    if AB == CD:
        ans += dic[AB]*dic[CD]
    else:
        ans += dic[AB]*dic[CD]*2
    
print(ans)