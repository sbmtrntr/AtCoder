from itertools import combinations
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

ans = 0

group = [[]for _ in range(100)]

dic = {}
for x in A:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

for num in A:
    for mod in range(1, 100):
        if num % mod == 0:
            group[mod-1].append(num)

print(group)
for i in range(100):
    if i+1 <= len(group[i]):
        ans += len(list(combinations(group[i], i+1)))

for v in dic.values():
    ans += 2**v
    ans -= 
print(ans)
