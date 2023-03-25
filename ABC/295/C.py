from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)

for a in A:
    dic[a] += 1

ans = 0
for v in dic.values():
    ans += v // 2

print(ans)