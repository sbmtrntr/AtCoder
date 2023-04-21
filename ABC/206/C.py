N = int(input())

A = list(map(int, input().split()))

ans = N*(N-1)//2
dic = {}

for i in range(N):
    if A[i] not in dic:
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1

for v in dic.values():
    ans -= v*(v-1)//2

print(ans)

