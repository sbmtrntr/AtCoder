N = int(input())

dic = {}

for i in range(N):
    s, t = input().split()
    if s not in dic:
        dic[s] = (int(t), i+1)

ans = 0
for v in dic.values():
    ans = max(ans, v[0])

for v in dic.values():
    if v[0] == ans:
        print(v[1])
        break