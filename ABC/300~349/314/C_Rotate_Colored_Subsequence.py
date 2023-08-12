from collections import defaultdict
N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))
ans = [""]*N
dic = defaultdict(list)
for i in range(N):
    dic[C[i]].append(i)

for v in dic.values():
    for i in range(len(v)):
        ans[v[i]] = S[v[i-1]]

print("".join(ans))