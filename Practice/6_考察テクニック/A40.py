from math import comb
from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)

for i in range(N):
    dic[A[i]] += 1

ans = 0

for v in dic.values():
    ans += comb(v, 3)

print(ans)