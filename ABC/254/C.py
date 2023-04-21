from tokenize import group


N, K = map(int, input().split())
a = list(map(int, input().split()))

A = sorted(a)

groups = [[] for _ in range(K)]

for i in range(N):
    groups[i%K].append(a[i]) 

for g in groups:
    g.sort()

b = [groups[i%K][i//K] for i in range(N)]

if A == b:
    print("Yes")
else:
    print("No")
