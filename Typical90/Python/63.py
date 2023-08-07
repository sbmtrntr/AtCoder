from itertools import product
from collections import defaultdict
H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
ans = 0

for pro in product((0, 1), repeat=H):
    if sum(pro) == 0:
        continue
    dic = defaultdict(int)
    for j in range(W):
        flag = True
        memo = -1
        for i in range(H):
            if pro[i] == 0:
                continue
            if memo == -1:
                memo = P[i][j]
            else:
                if P[i][j] != memo:
                    flag = False
                    break
        if flag:
            dic[memo] += 1
            
    if any(dic):
        ans = max(ans, sum(pro) * max(dic.values()))

print(ans)