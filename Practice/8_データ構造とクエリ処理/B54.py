N = int(input())
dic = {}
ans = 0

for i in range(N):
    A = input()
    if A not in dic:
        dic[A] = 0
    else:
        dic[A] += 1

for v in dic.values():
    ans += v*(v+1) // 2

print(ans)