import sys
sys.setrecursionlimit(10**6)


N = int(input())

dic = {}
memo = set()
for _ in range(N):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)
    memo.add(a)
    memo.add(b)

ans = 1

def dfs(n, lis):
    global ans
    for num in lis:
        ans = max(num, ans)
        if num in dic and num in memo:
            memo.remove(num)
            dfs(num, dic[num])

    return ans

if 1 not in dic: print(ans)
else: print(dfs(1, dic[1]))